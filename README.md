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
📁 Output Example 
Given: 
Base: admin
Suffix: !
Max length: 12

📜 Logging 
All actions are logged to: 
Console (INFO+ level)
File: logs/word_logs.log (DEBUG+ level)


2024-06-10 14:30:00 | INFO | Beginning wordlist generation...
2024-06-10 14:30:01 | DEBUG | Add password: Admin!
2024-06-10 14:30:01 | INFO | Was generated 3 passwords~!
2024-06-10 14:30:01 | INFO | File wordlists/my_wordlist.txt was created!

🛡️ Disclaimer 
This tool is intended for ethical and authorized security testing only.
Do not use it to attack systems without explicit permission. 

▶️ Usage 
Basic Example 
python wordlist_gen.py --base "admin,user,root" --suffix "!,123" --output my_wordlist.txt

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Bandihok/wordlist-generator.git
   cd wordlist-generator
