# 🔐 Coding-Decoding Application

A Python-based command-line application that transforms text using custom character-shifting, text-reversal, and random-character techniques.

This project is being developed to practise Python programming, logical thinking, and modular software development.

## ✨ Features

- **Custom Encoding:** Transforms characters according to predefined character sequences.
- **Text Reversal:** Reverses the message as part of the transformation process.
- **Random Character Sequences:** Generates random characters to use as prefixes and suffixes.
- **Decoding:** Restores the encoded message using the corresponding decoding logic.
- **Lowercase Output:** Converts alphabetic characters to lowercase during encoding. The decoded output is also lowercase; original uppercase letters are not preserved.
- **Command-Line Interface:** Provides a menu to choose between encoding, decoding, and exiting.
- **Modular Structure:** Separates the encoding, decoding, and main program into individual Python files.

> **Note:** Features should be considered complete only after they have been implemented and tested successfully.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Standard Library:** `random`
- **Development Environment:** Visual Studio Code

## 📁 Project Structure

```text
Coding-Decoding/
├── main.py
├── encoding.py
├── decoding.py
├── README.md
└── .gitignore
```

- `main.py` — Provides the main menu and connects the program's components.
- `encoding.py` — Contains the encoding logic.
- `decoding.py` — Contains the decoding logic.
- `README.md` — Documents the project.
- `.gitignore` — Specifies files that Git should ignore.

Python may automatically generate a `__pycache__/` directory while running the application. These cache files should be excluded from version control through `.gitignore`.

## 🚀 Getting Started

### Prerequisites

- Python 3 installed on your system.
- A code editor or terminal.

### Installation

1. Download or clone this repository.
2. Open the project folder in your code editor.
3. Ensure that `main.py`, `encoding.py`, and `decoding.py` are in the same directory.

### Run the Application

Open a terminal in the project directory and run:

```bash
python3 main.py
```

On Windows, you may also use:

```bash
python main.py
```

Follow the on-screen instructions to select an operation.

## ⚠️ Security Notice

**Educational Use Only:** This application uses custom text transformations and obfuscation techniques. It is not a cryptographically secure encryption system and should not be used to protect passwords, confidential messages, or other sensitive information.

**Important limitations:**

- Alphabetic characters are converted to lowercase. Original uppercase and lowercase distinctions cannot be recovered.
- Random prefixes and suffixes are used as part of the encoding process; they do not provide meaningful cryptographic security.
- The decoder does not reliably verify whether an input is genuinely encoded or has been modified.
- Successful decoding depends on the encoding and decoding algorithms using matching character sequences and transformation rules.

## 🔮 Planned Improvements

- Complete and thoroughly test the decoding functionality.
- Improve input validation and error handling.
- Test handling of spaces, punctuation, digits, and other supported characters.
- Add automated tests for encoding and decoding.
- Improve the command-line interface and overall usability.

## 👨‍💻 Author

**Mohammed Nasif Ansari**

Created as a Python learning project to practise lists, indexing, loops, conditionals, functions, randomisation, and modular programming.

---

*Built with Python 🐍*
