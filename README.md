# 🔐 Password Manager & Generator

A secure local password manager written in Python.
Stores your credentials in an **AES-encrypted vault** and includes a strong password generator.

## ✨ Features
- 🔑 Master-password protected vault (AES-256)
- 🧰 Add, retrieve, and delete credentials
- 🔒 Passwords encrypted locally (no server, no cloud)
- 🎲 Random strong password generator
- ✅ Implemented in pure Python

## 📂 Project Structure
- `password_manager.py` – Main CLI
- `crypto_utils.py` – Encryption helpers
- `storage.py` – Vault file management
- `data/` – Encrypted vault & salt
- `tests/` – Unit tests

## 🚀 How to Run
```bash
git clone https://github.com/manasp17/password-manager.git
cd password-manager
pip install -r requirements.txt
python password_manager.py

🔧 Requirements
Python 3.10+

cryptography library

