# 🔐 TOTP OTP Generator

A simple Python project that generates a **TOTP secret**, creates a **QR code** for authenticator apps, and verifies OTP codes.

## 📦 Installation

```bash
pip install pyotp qrcode[pil]
```

## 🚀 Usage

Run:

```bash
python main.py
```

Enter your account name, scan the generated `otp_qr.png` with an authenticator app, then enter the generated OTP code.

## 🛠️ Requirements

* Python 3.x
* pyotp
* qrcode
* Pillow

## 📄 License

MIT
