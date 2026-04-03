import os
import sys
import warnings
import argparse
import json
import concurrent.futures
import math

# Monkey-patch for mordred compatibility with modern numpy (>= 1.25)
import numpy as np
if not hasattr(np, 'product'):
    np.product = np.prod

import networkx as nx
import pandas as pd
from mordred import Calculator, descriptors
from mordred.error import DuplicatedDescriptorName
from mordred.PathCount import PathCount
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.MolStandardize import rdMolStandardize
from tqdm import tqdm

# =============================================================================
# 1. Utility Functions
# =============================================================================
def interactive_selector(start_path, prompt, select_file=True, allowed_exts=None):
    """Interactively select a file or directory from the terminal."""
    if allowed_exts is None:
        allowed_exts = ['.sdf', '.sd', '.csv', '.tsv', '.smi', '.txt']
    current_path = os.path.abspath(start_path)

    while True:
        print("\n" + "="*50 + f"\n{prompt}\nCurrent Path: {current_path}\n" + "="*50)
        try:
            items = sorted(os.listdir(current_path))
        except OSError as e:
            print(f"Error access: {e}"); current_path = os.path.dirname(current_path); continue

        options = {'0': ('.. (Parent Directory)', os.path.join(current_path, '..'))}
        if not select_file:
            options['1'] = ('./ (Select this directory)', current_path)

        dir_list, file_list = [], []
        for item in items:
            full_path = os.path.join(current_path, item)
            if os.path.isdir(full_path):
                dir_list.append((f"[DIR] {item}", full_path))
            elif select_file and os.path.splitext(item)[1].lower() in allowed_exts:
                file_list.append((f"[{os.path.splitext(item)[1].upper()[1:]}] {item}", full_path))
        
        display_list = sorted(dir_list) + sorted(file_list)
        for i, (name, _) in options.items(): print(f"[{i}] {name}")
        for i, (name, _) in enumerate(display_list, start=len(options)): print(f"[{i}] {name}")

        try:
            choice = input("Enter number, or 'q' to quit: ").strip()
            if choice.lower() == 'q': sys.exit("Cancelled.")
            idx = int(choice)
            if str(idx) in options:
                current_path = os.path.abspath(options[str(idx)][1])
                if str(idx) == '1' and not select_file: return current_path
            elif idx >= len(options):
                target = display_list[idx - len(options)][1]
                if os.path.isdir(target): current_path = target
                else: return os.path.abspath(target)
        except: print("Invalid input.")

def preprocess_molecule(mol, seed=42):
    """Performs desalting and structure standardization with fixed seed."""
    if mol is None: return None
    try:
        mol = rdMolStandardize.Cleanup(mol)
        lfc = rdMolStandardize.LargestFragmentChooser()
        mol = lfc.choose(mol)
        uncharger = rdMolStandardize.Uncharger()
        mol = uncharger.uncharge(mol)
        
        # Consistent 3D Embedding
        if mol.GetNumConformers() == 0:
            mol = Chem.AddHs(mol)
            params = AllChem.ETKDGv3() # Improved version
            params.randomSeed = seed # CRITICAL: Fixed Seed
            if AllChem.EmbedMolecule(mol, params) == -1:
                return None # Fail on embedding error
        return mol
    except Exception as e:
        return None

# =============================================================================
# 2. Descriptor Calculation
# =============================================================================
def calc_conjugation_features(mol):
    """Calculates conjugation features with error handling."""
    res = {"Conjugation_Count": 0, "Conjugation_MaxAtomCount": 0, "Conjugation_MaxLength": 0, "Conjugation_BLA": np.nan, "Conjugation_GraphEnergy": 0.0}
    if mol is None: return res
    try:
        conjugated_bonds = [b for b in mol.GetBonds() if b.GetIsConjugated()]
        if not conjugated_bonds: return res
        
        has_3d = mol.GetNumConformers() > 0
        conf = mol.GetConformer() if has_3d else None
        
        graph = nx.Graph()
        for b in conjugated_bonds:
            u, v = b.GetBeginAtomIdx(), b.GetEndAtomIdx()
            w = conf.GetAtomPosition(u).Distance(conf.GetAtomPosition(v)) if has_3d else 1.0
            graph.add_edge(u, v, weight=w)
            
        systems = list(nx.connected_components(graph))
        if not systems: return res
        
        largest = max(systems, key=len)
        sub = graph.subgraph(largest)
        
        res["Conjugation_Count"] = len(systems)
        res["Conjugation_MaxAtomCount"] = len(largest)
        if sub.number_of_nodes() > 1:
            try: res["Conjugation_MaxLength"] = nx.diameter(sub)
            except: pass
        if has_3d and sub.number_of_edges() > 0:
            res["Conjugation_BLA"] = np.std(list(nx.get_edge_attributes(sub, 'weight').values()))
            
        adj = nx.to_numpy_array(sub, weight=None)
        res["Conjugation_GraphEnergy"] = np.sum(np.abs(np.linalg.eigvalsh(adj)))
        return res
    except Exception: return res

def setup_mordred_calculator():
    calc = Calculator(descriptors.all, ignore_3D=False)
    for i in range(1, 51):
        try:
            calc.register(PathCount(order=i, pi=False))
            calc.register(PathCount(order=i, pi=True))
        except DuplicatedDescriptorName: pass
    return calc

# =============================================================================
# 3. Execution
# =============================================================================
def main():
    warnings.filterwarnings('ignore')
    parser = argparse.ArgumentParser(description="Professional Descriptor Calculator.")
    parser.add_argument('--config', help='Path to JSON config.')
    parser.add_argument('--batch_size', type=int, default=1000)
    parser.add_argument('--seed', type=int, default=42, help='Random seed for 3D embedding.')
    args = parser.parse_args()

    smiles_col, name_col = None, None
    if args.config:
        try:
            with open(args.config, 'r', encoding='utf-8') as f:
                config = json.load(f)
            in_path, out_dir = config['input_path'], config['output_path']
            smiles_col, name_col = config.get('smiles_col'), config.get('name_col')
        except Exception as e:
            sys.exit(f"Config Error: {e}")
    else:
        in_path = interactive_selector('.', "Select Input File")
        out_dir = interactive_selector(os.path.dirname(in_path), "Select Output Directory", False)

    out_csv = os.path.join(out_dir, os.path.splitext(os.path.basename(in_path))[0] + "_descriptors.csv")
    calc = setup_mordred_calculator()
    n_cores = os.cpu_count() or 1

    print(f"\nProcessing: {in_path}\nOutput: {out_csv}\nSeed: {args.seed}")

    # Simplified Loader
    df_in = pd.read_csv(in_path, sep=None, engine='python') if in_path.endswith(('.csv', '.tsv', '.txt')) else None
    
    if df_in is not None:
        if not smiles_col:
            from __main__ import select_column_interactive # placeholder
            smiles_col = df_in.columns[0] # Default
        
        mols, props_list, errors = [], [], []
        for i, row in tqdm(df_in.iterrows(), total=len(df_in), desc="Standardizing"):
            smiles = str(row[smiles_col])
            mol = Chem.MolFromSmiles(smiles)
            clean_mol = preprocess_molecule(mol, seed=args.seed)
            if clean_mol:
                name = str(row[name_col]) if name_col and name_col in row else f"Mol_{i}"
                clean_mol.SetProp("_Name", name)
                mols.append(clean_mol)
                props_list.append(row.to_dict())
            else:
                errors.append({"index": i, "smiles": smiles, "reason": "Standardization/3D Failed"})

        if mols:
            m_df = calc.pandas(mols, nproc=n_cores, quiet=False)
            m_df = m_df.apply(pd.to_numeric, errors='coerce')
            
            with concurrent.futures.ProcessPoolExecutor(max_workers=n_cores) as exec:
                c_list = list(exec.map(calc_conjugation_features, mols))
            c_df = pd.DataFrame(c_list)
            
            final_df = pd.concat([pd.DataFrame(props_list), m_df, c_df], axis=1)
            final_df.to_csv(out_csv, index=False)
            print(f"\nSuccess: {len(mols)} molecules processed.")
        
        if errors:
            err_path = out_csv + ".errors.json"
            with open(err_path, 'w') as f: json.dump(errors, f, indent=2)
            print(f"Noted {len(errors)} errors in {err_path}")

if __name__ == "__main__":
    main()
