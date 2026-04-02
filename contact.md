---
layout: default
title: Contact
---

<div data-lang-content="ja" markdown="1">

# お問い合わせ (Contact)

[← ホームに戻る](/index)

共同研究、発表のご依頼、その他お問い合わせは以下のフォームよりお気軽にご連絡ください。  
※送信内容は暗号化されて安全に管理されます。

<div class="contact-box">
    <form action="https://formspree.io/f/mvzvbodq" method="POST">
        <div class="form-group">
            <label>お名前</label>
            <input type="text" name="name" placeholder="山田 太郎" required>
        </div>
        <div class="form-group">
            <label>メールアドレス</label>
            <input type="email" name="email" placeholder="your@email.com" required>
        </div>
        <div class="form-group">
            <label>件名</label>
            <input type="text" name="subject" placeholder="共同研究について" required>
        </div>
        <div class="form-group">
            <label>メッセージ内容</label>
            <textarea name="message" rows="5" placeholder="こちらに詳細をご記入ください" required></textarea>
        </div>
        <!-- 成功時のリダイレクト先 -->
        <input type="hidden" name="_next" value="https://377h-miru.github.io/contact">
        <button type="submit" class="submit-btn">送信する</button>
    </form>
</div>

</div>

<div data-lang-content="en" markdown="1">

# Contact

[← Back to Home](/index)

For research collaborations, speaking invitations, or other inquiries, please use the form below.

<div class="contact-box">
    <form action="https://formspree.io/f/mvzvbodq" method="POST">
        <div class="form-group">
            <label>Name</label>
            <input type="text" name="name" placeholder="John Doe" required>
        </div>
        <div class="form-group">
            <label>Email Address</label>
            <input type="email" name="email" placeholder="your@email.com" required>
        </div>
        <div class="form-group">
            <label>Subject</label>
            <input type="text" name="subject" placeholder="Collaboration Inquiry" required>
        </div>
        <div class="form-group">
            <label>Message</label>
            <textarea name="message" rows="5" placeholder="Enter your message here" required></textarea>
        </div>
        <input type="hidden" name="_next" value="https://377h-miru.github.io/contact">
        <button type="submit" class="submit-btn">Send Message</button>
    </form>
</div>

</div>
