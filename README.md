# Secure Insurance Management System – SAST Review & Remediation

A security-hardened version of an open-source, console-based **Python insurance management system** (customers, policies and claims stored in MySQL).

The goal of this project was **secure code review**: find the vulnerabilities in the original application with **static analysis (SAST)** and manual code review, fix them, and confirm the fixes by re-scanning.

> Application Security coursework. The base application is the open-source [Insurance_Managment_System_Py](https://github.com/NikylS007/Insurance_Managment_System_Py) by **NikylS007**; the security analysis and every fix described below are my own work.

---

## Process

1. **Scan**: ran Bandit, Semgrep and Snyk on the original code, then reviewed it manually.
2. **Prioritise**: mapped the findings to CWE and picked the three highest-impact issues.
3. **Fix**: rewrote the affected code with secure alternatives.
4. **Verify**: re-ran Bandit and tested by hand to confirm the issues were closed.

## Vulnerabilities Fixed

| # | Vulnerability | CWE | Before | After |
|---|---|---|---|---|
| 1 | **Hardcoded credentials** | CWE-259 / CWE-798 | Database and agent passwords written in plain text in the source code | Secrets loaded from a git-ignored `.env` file with `python-dotenv` |
| 2 | **Weak random number generation** | CWE-330 | `random.sample()` used to generate Customer and Policy IDs | Cryptographically secure `secrets` module (`secrets.choice`, `secrets.token_hex`) |
| 3 | **Plaintext password storage / comparison** | CWE-522 | Agent password compared directly against a plain-text value | Agent password stored as a **bcrypt hash** and checked with `bcrypt.checkpw()`; helper script to generate the hash |

Other hardening:
- Regex-based **input validation** on menu options, names and passwords.
- **Parameterised SQL queries** (`%s` placeholders) for inserts.
- `.gitignore` keeps the `.env` file out of version control.

**Result:** after the fixes, the Bandit re-scan no longer reports the hardcoded password (B105) or insecure random (B311) findings.

---

## Tech Stack
Python · MySQL (`mysql-connector-python`) · bcrypt · python-dotenv · PrettyTable
**Security tools:** Bandit · Semgrep · Snyk

## Getting Started

```bash
git clone https://github.com/sultanrabea4/secure-insurance-management-system.git
cd secure-insurance-management-system
pip install -r requirements.txt

# Generate a bcrypt hash for the agent password
python generate_agent_hash.py

# Create your .env from the template and paste the hash
copy .env.example .env

# MySQL must be running locally
python main.py
```

## Project Structure
```
├── main.py                  # entry point
├── Methods.py               # menus, authentication, database access
├── Policy.py                # policy creation and premium calculation
├── Customer.py              # customer model
├── generate_agent_hash.py   # creates the bcrypt hash for the agent password
└── .env.example             # template for secrets
```

## Future Improvements
- Hash **customer** passwords with bcrypt as well (the scope of this assessment covered the agent credentials).
- Use a least-privilege database user instead of `root`.

## Author
**Sultan Mohammed Rabea** · [LinkedIn](https://www.linkedin.com/in/sultan-rabea/) · [GitHub](https://github.com/sultanrabea4)
