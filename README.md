# 🔐 Wordlist Generator with Logging & Config

A flexible and configurable Python script to generate custom wordlists by combining base words with suffixes. Supports case variations (lower, upper, capitalized), length filtering, and logs all operations to both console and file.

Perfect for penetration testing, password strength analysis, or educational purposes.

---

## 🚀 Features

- ✅ Generate passwords from base words + suffixes  
- ✅ Automatic case variations: `lower`, `UPPER`, `Capitalize`  
- ✅ Configurable maximum password length  
- ✅ Dual logging: console + file (`logs/word_logs.log`)  
- ✅ Configurable via `config.ini`  
- ✅ CLI arguments with defaults from config  
- ✅ Automatic directory creation for output  

---

## 🛠️ Requirements

- Python 3.6+

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Bandihok/wordlist-generator.git
   cd wordlist-generator
