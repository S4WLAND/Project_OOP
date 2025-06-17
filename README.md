# 🎓 Academic Record Manager 🐍

<!-- Badges -->
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-Interactive-8E44AD?style=for-the-badge)

---

**Academic Record Manager** is a lightweight Python + SQLite command-line app that lets you create subjects, register students, record grades and instantly calculate weighted GPAs.  
Originally a college assignment, it evolved into a full CRUD sandbox for practising OOP patterns, error handling and SQL operations in pure Python.

---

## 🚀 Features

- 📚 **Subjects** – add / edit / delete courses with credit weighting  
- 👩‍🎓 **Students** – register and manage personal data  
- 📝 **Academic History** – link students & subjects, store final grades  
- 🏅 **GPA Ranking** – auto-compute GPA and total credits per student  
- 🔒 **Interactive CLI** – nested menus, input validation & friendly errors  

---

## 📂 Project Layout

\`\`\`
proyecto_promedio_academico.py   # all-in-one script (OOP + CLI + SQLite)
README.md                        # you are here
\`\`\`

---

## 🛠 Tech Stack

| Icon | Tool        | Purpose                          |
|------|-------------|----------------------------------|
| 🐍   | Python 3.10+ | Core language & CLI logic        |
| 🗄️   | SQLite3      | Embedded relational database     |
| 🧩   | OOP          | Classes: Subject, Student, Record|
| 🐞   | try/except   | Robust input & error handling    |

---

## ▶️ Quick Start

\`\`\`bash
# clone the repo
git clone https://github.com/S4WLAND/Project_OOP.git
cd academic-record-manager

# (optional) create virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# run the application
python proyecto_promedio_academico.py
\`\`\`

A local **\`MI_BDD.db\`** file will be generated automatically.

---

## ✨ Example Workflow

1. **Subjects → Insert** – register “Data Structures” (3 credits).  
2. **Students → Insert** – add student *Jane Doe*.  
3. **Academic History → Create** – assign Jane’s grade (4.3 / 5.0).  
4. **Classification → Consult** – view Jane’s GPA and credit summary.

---

## 👤 Author

Made with ☕ & 💡 by **Stifh BL** — Software Developer and lifelong learner.

---

## 📜 License

Released under the **MIT License** — feel free to use, modify and share!
