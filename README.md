# 🛡️ Gostyy Forensic Lab

> **Interactive Code Vulnerability & Forensic Log Analyzer using Pattern Matching & Heuristic Rules**

`Gostyy Forensic Lab` is an interactive security auditing and digital forensics web application. Built with Streamlit and powered by AI/Regex heuristic engines, it detects critical security flaws, hardcoded credentials, and code injection vulnerabilities in real-time with an immersive, glassmorphism-inspired interface.

---

## ⚡ Features

* **🔍 Multi-Vector Threat Detection:** Scans source code for SQLi, Command Injection, XSS, Path Traversal, and SSRF.
* **🔑 Secret & API Key Leak Prevention:** Identifies hardcoded cryptographic keys, tokens, and insecure hashing mechanisms.
* **🧠 Context-Aware Vulnerability Scoring:** Provides instant severity ratings and rule-based remediation guidance.
* **🖥️ Cyberpunk Glassmorphism UI:** Features dynamic feedback, status logs, and custom visual effects for security analysts.
* **📊 Comprehensive Forensic Reports:** Generates structured findings with integrity verification.

---

## 📸 Demo & Preview

*Live Streamlit Deployment:*  
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gostyy-forensic-lab.streamlit.app/)

 
![Forensic Lab](assets/Animation.gif)

---

## 🎯 Detected Vulnerability Vectors

| Category | Vulnerability Type | Severity |
| :--- | :--- | :--- |
| **Injection** | SQL Injection (SQLi) | 🔴 HIGH |
| **Execution** | Arbitrary Command Injection | 🔴 HIGH |
| **Secrets** | Hardcoded API Keys / Credentials | 🔴 HIGH |
| **Web Safety** | Cross-Site Scripting (XSS) | 🟠 MEDIUM |
| **File System** | Path Traversal / File Inclusion | 🟠 MEDIUM |
| **Crypto** | Weak Hashes (MD5 / SHA1) & `eval()` | 🟠 MEDIUM |
| **Auth & Access**| SSRF / IDOR / Missing Auth | 🟡 LOW |

---

## 🛠️ Tech Stack & Prerequisites

* **Language:** Python 3.x
* **Framework:** Streamlit
* **Security & Parsing:** Regex Heuristics / Anthropic API Integration

---

## 🚀 Quick Start

### 1. Clone the repository:
```bash
git clone [https://github.com/gostyy8/Gostyy-Forensic-Lab.git](https://github.com/gostyy8/Gostyy-Forensic-Lab.git)
cd Gostyy-Forensic-Lab
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables (Optional for AI analysis):
```bash
# Windows (PowerShell):
$env:ANTHROPIC_API_KEY="your-api-key-here"

# Linux/Mac:
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 4. Run the Streamlit dashboard:
```bash
streamlit run app.py
```

