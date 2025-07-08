# 🔐 Smart Leet Password Generator

A powerful password list generator built in Python that simulates how real-world attackers generate wordlists from social engineering data.  
It creates **1,000,000 customized passwords** based on user input with smart `leet` (1337) character substitutions.

---

## 📌 Features

- 🔣 Replaces characters with symbols:  
  - `a` → `@`  
  - `i`, `l` → `!`  
  - `s` → `$`  
  - `gh` → `8`  
  - `o` → `0`  
  - `e` → `3`

- 🔐 Adds 2+ special characters in every password  
- 🔄 Supports random combinations of:
  - Nickname
  - Favorite number
  - Custom words (pet names, dates, etc.)
  - Extra optional inputs  
- ✅ Guarantees passwords like `Mazen_1234@@`, `M@z3n_1234!!`, etc.
- 📏 Max password length: 16 characters
- 💥 Outputs **1 million unique passwords** in `leet_passwords.txt`

---

## 🚀 How to Use

### ✅ Requirements

- Python 3.6+
- No external libraries needed

### ▶️ Run the script

```bash
python leet_password_generator.py
