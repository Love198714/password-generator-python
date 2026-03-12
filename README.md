README.md
# 🛡️ Hilda's Tech Haven: Password Generator

A professional CLI tool built in Python for generating cryptographically secure, customizable passwords.

## 🚀 Features
* **Secure:** Uses the `secrets` module for high-entropy randomness.
* **Audit:** Includes a 1-to-5 star strength rating system.
* **Bulk:** Generate multiple passwords at once.

## 📖 Usage Guide

Run the script using these flags:

| Flag | Description |
| :--- | :--- |
| `-t` | Total password length |
| `-a` | Amount of passwords to generate |
| `-o` | Output to a .txt file |

### Example Command
`python password_generator.py -t 16 -a 5`

---

## 📡 Port Scanner
A network discovery tool that checks for open TCP ports on a target IP address.

### Features
* **Range Scanning:** Scan a specific range of ports (e.g., 1-100).
* **Interactive:** Prompts for Target IP and Port Range.
* **Color Output:** Uses ANSI codes to highlight open ports.

### Usage
`python port_scanner.py`