---
layout: default
title: Contact
---

<div data-lang-content="ja" markdown="1">

# お問い合わせ (Contact)

[← ホームに戻る](/)

共同研究、発表のご依頼、その他お問い合わせは以下のフォームよりご連絡ください。

<div class="contact-box">
    <!-- Success/Error Messages -->
    <div data-fs-success style="display:none; color: #2da44e; margin-bottom: 20px; font-weight: bold;">
        メッセージをお送りいただきありがとうございます。内容を確認次第、ご連絡いたします。
    </div>
    <div data-fs-error style="display:none; color: #cf222e; margin-bottom: 20px; font-weight: bold;">
        送信中にエラーが発生しました。入力内容を確認して再度お試しください。
    </div>

    <form id="contact-form">
        <div class="form-group">
            <label>お名前</label>
            <input type="text" name="name" placeholder="山田 太郎" data-fs-field required>
            <span data-fs-error="name" style="color: #cf222e; font-size: 0.85em;"></span>
        </div>
        <div class="form-group">
            <label>メールアドレス</label>
            <input type="email" name="email" placeholder="your@email.com" data-fs-field required>
            <span data-fs-error="email" style="color: #cf222e; font-size: 0.85em;"></span>
        </div>
        <div class="form-group">
            <label>件名</label>
            <input type="text" name="subject" placeholder="共同研究について" data-fs-field required>
            <span data-fs-error="subject" style="color: #cf222e; font-size: 0.85em;"></span>
        </div>
        <div class="form-group">
            <label>メッセージ内容</label>
            <textarea name="message" rows="5" placeholder="こちらに詳細をご記入ください" data-fs-field required></textarea>
            <span data-fs-error="message" style="color: #cf222e; font-size: 0.85em;"></span>
        </div>
        <button type="submit" class="submit-btn" data-fs-submit-btn>送信する</button>
    </form>
</div>

#### 個人情報の取り扱いについて
ご入力いただいた個人情報（お名前、メールアドレス）は、お問い合わせに対する回答および必要な情報の提供にのみ利用し、適切に管理いたします。

</div>

<div data-lang-content="en" markdown="1">

# Contact

[← Back to Home](/)

For research collaborations, speaking invitations, or other inquiries, please use the form below.

<div class="contact-box">
    <!-- Success/Error Messages -->
    <div data-fs-success style="display:none; color: #2da44e; margin-bottom: 20px; font-weight: bold;">
        Thank you for your message. I will get back to you as soon as possible.
    </div>
    <div data-fs-error style="display:none; color: #cf222e; margin-bottom: 20px; font-weight: bold;">
        An error occurred while sending. Please check your input and try again.
    </div>

    <form id="contact-form-en">
        <div class="form-group">
            <label>Name</label>
            <input type="text" name="name" placeholder="John Doe" data-fs-field required>
            <span data-fs-error="name" style="color: #cf222e; font-size: 0.85em;"></span>
        </div>
        <div class="form-group">
            <label>Email Address</label>
            <input type="email" name="email" placeholder="your@email.com" data-fs-field required>
            <span data-fs-error="email" style="color: #cf222e; font-size: 0.85em;"></span>
        </div>
        <div class="form-group">
            <label>Subject</label>
            <input type="text" name="subject" placeholder="Collaboration Inquiry" data-fs-field required>
            <span data-fs-error="subject" style="color: #cf222e; font-size: 0.85em;"></span>
        </div>
        <div class="form-group">
            <label>Message</label>
            <textarea name="message" rows="5" placeholder="Enter your message here" data-fs-field required></textarea>
            <span data-fs-error="message" style="color: #cf222e; font-size: 0.85em;"></span>
        </div>
        <button type="submit" class="submit-btn" data-fs-submit-btn>Send Message</button>
    </form>
</div>

#### Privacy Note
The personal information provided (name, email) will be used solely for responding to your inquiry and will be managed securely.

</div>

<!-- Formspree Ajax Integration -->
<script>
  window.formspree = window.formspree || function () { (formspree.q = formspree.q || []).push(arguments); };
  formspree('initForm', { formElement: '#contact-form', formId: 'mvzvbodq' });
  formspree('initForm', { formElement: '#contact-form-en', formId: 'mvzvbodq' });
</script>
<script src="https://unpkg.com/@formspree/ajax@1" defer></script>
