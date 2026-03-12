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

---

## 🛡️ Hash Generator
A data integrity tool that generates unique SHA-256 digital fingerprints for any text input.

### Features
* **Industry Standard:** Uses the SHA-256 cryptographic algorithm.
* **Integrity Checking:** Demonstrates how even a minor change alters the entire output.
* **Clean UI:** Highlights the hash result in terminal green.

### Usage
`python hash_generator.py`

---

## 👃 DHCP Network Sniffer
A real-time network monitoring tool that captures DHCP packets to identify new devices connecting to the local network.

### Features
* **Live Discovery:** Captures MAC addresses, hostnames, and requested IPs.
* **Audit Logging:** Automatically saves all connection events to `network_audit_log.txt` for forensic review.
* **Layer Analysis:** Deep packet inspection of Ethernet and DHCP layers using `Scapy`.

### Usage
*Note: This tool requires Administrator/Root privileges to access network hardware.*
`python dhcp_listener.py`

# 🛡️ Hilda's Tech Haven: Security Suite

A modular Python framework for local cybersecurity operations, featuring automated network monitoring, cryptographic auditing, and secure credential generation.

## 🚀 Features
- **Secure Gatekeeper:** Password-protected CLI with masked input using `getpass`.
- **Elite Password Generator:** High-entropy credential creator with strength scoring.
- **DHCP Network Sniffer:** Real-time device discovery and logging using `Scapy`.
- **Hash Integrity Auditor:** SHA-256 file verification for digital forensics.
- **Port Scanner:** Automated reconnaissance tool for network mapping.

## 🛠️ Concepts Applied
- **IAM (Identity & Access Management):** Access control via authentication.
- **Packet Analysis:** Monitoring OSI Layer 2/Layer 7 traffic.
- **Digital Forensics:** Establishing an audit trail for network connections.
- **Automation:** Managing child processes with the `subprocess` module.