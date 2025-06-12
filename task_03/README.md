# 🔐 Secure Flask Login System

A professional demonstration project showcasing how to identify and remediate common security vulnerabilities in a basic Python Flask login system.

This project covers real-world secure coding practices and integrates industry tools for auditing and hardening the codebase.

---

## 🛠 Tech Stack

- 🐍 Python 3.x  
- 🌐 Flask (Web Framework)  
- 🗄 SQLite (Database)  
- 🔐 Werkzeug Security (for password hashing)  
- 📦 python-dotenv (for secret key management)

---

## ⚠️ Security Vulnerabilities Fixed

| Vulnerability | Description | Status |
|---------------|-------------|--------|
| SQL Injection | Unvalidated string interpolation in SQL queries | ✅ Mitigated using parameterized queries |
| Hardcoded Secret Keys | Secret key stored in source code | ✅ Replaced with environment variables |
| Plaintext Passwords | Storing raw passwords in DB | ✅ Encrypted using `check_password_hash` |
| Session Fixation | Session hijacking risk post-login | ✅ Session cleared on authentication |
| No HTTPS | Lack of secure transport layer | ⚠️ Requires deployment-level HTTPS (e.g., Flask-Talisman or proxy config)

---

## 🔧 Tools Used for Security Analysis

- 🛡 [`Bandit`](https://github.com/PyCQA/bandit) – Python static code analyzer
- 🔎 [`Safety`](https://github.com/pyupio/safety) – Detect known vulnerabilities in dependencies
- ✨ [`Flake8`](https://flake8.pycqa.org/) – Code style and quality checker

---

## 📄 How to Run the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/secure-flask-login.git
cd secure-flask-login
````

### 2. Create `.env` File

```env
SECRET_KEY=your-secure-random-key
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
flask run
```

> Visit `http://127.0.0.1:5000/login` in your browser.

---

## 📊 Security Reports

The following automated audit reports are included for transparency:

* `bandit_report.txt` – Static code analysis
* `safety_report.txt` – Vulnerable dependencies
* `flake8_report.txt` – Code quality and style

---

## ✅ Secure Coding Practices Implemented

* ✅ Input validation via parameterized queries
* ✅ Secrets managed with `.env` and not hardcoded
* ✅ Passwords hashed using `Werkzeug` library
* ✅ Session cleared on login to prevent fixation
* ✅ Integrated static and dependency security analysis tools

---

## 💡 Future Enhancements

* Add HTTPS enforcement using Flask-Talisman or deploy behind a secure proxy (e.g., NGINX)
* Implement rate-limiting and account lockout
* Use JWT or OAuth for token-based authentication
* Dockerize the application for container-based deployment

---

🔗 View the project on GitHub: [github.com/yourusername/secure-flask-login]
## 📌 License

This project is open-source under the [MIT License](LICENSE).

```

---

### ✅ What's Included & Improved:
- Fully structured markdown syntax
- Clear, professional language
- Code blocks for easier copy/paste
- Links to tools and GitHub best practices
- Sections for future scope and licensing


