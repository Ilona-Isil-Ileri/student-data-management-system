# Student & Course Data Management System (Python) 🎓

A simple, file-based Python script that processes student records, course info, and grades from text files.  
This project was built to demonstrate basic **programming logic, working with text files (.txt), input validation, and using AI as a learning and debugging assistant**.

---

## 📌 Project Overview
The goal of this script is to manage and connect basic student data, course enrollments, course instructor records, and grading histories stored across separate text files (`.txt`).

Instead of complex databases, this project focuses on foundational programming concepts: reading from files, validating user inputs, and structuring a terminal-based menu system.

### Data Files Used:
- **`students.txt`**: Stores basic student information (IDs, names, emails, etc.).
- **`courses.txt`**: Stores course details and assigned instructors.
- **`passed.txt`**: Stores student course completion records, dates, and grades.

### Examples of Key Features:
- **Text File Processing:** Reads, searches, and cross-references data between text files.
- **Input Validation & Error Handling:** Uses `try/except` blocks and basic checks (e.g., date formats, capitalizations) to avoid errors.
- **Calculations:** Calculates total ECTS credits and GPA averages based on student completion records.
- **Record Updating:** Safely updates and writes new course completion grades to the files without deleting existing data.

---

## 🛠️ Core Functions & Structure

1. `add_student()`: Generates unique student IDs, validates name formats, creates a standardized student email format, and appends valid entries.
2. `search_student()`: Searches for students case-insensitively and handles matches using structured list formats.
3. `search_course()`: Searches course information and lists the assigned teachers properly.
4. `add_course_completion()`: Validates date and grade inputs, handles historical dates, then updates the student's passing record safely.
5. `show_student_record()`: Gathers student info, calculates total ECTS and GPA, and prints a clean formatted transcript/summary (handling edge cases like missing middle names).

---

## 🤖 AI Assistance & Learning Process

This project was built using **ChatGPT** as a guidance and learning assistant. Rather than generating raw code blindly, I used AI to understand the logic step-by-step:

- **Planning & Structure:** Guided me on how to break down the project into functions, which function to start with, and set up a basic menu loop (`while` and `if` logic).
- **Debugging & Fixing Bugs:** Helped solve why loops weren't matching inputs or why files were overwriting incorrectly.
- **Translating Ideas & Pseudocode:** Helped turn my thoughts and self-written basic pseudocode into working Python syntax.
- **Learning Best Practices:** Taught me basic habits like handling file paths, using `try/except`, and keeping code readable as a beginner.

> **Note:** All structural and implementation decisions were reviewed and understood by me. The AI acted as a mentor/tutor during the process.

---

## 🚀 How to Run

1. Clone or download this repository:
   [https://github.com/Ilona-Isil-Ileri/student-data-management-system.git](https://github.com/Ilona-Isil-Ileri/student-data-management-system.git)
2. Make sure the .txt data files (students.txt, courses.txt, passed.txt) are in the same folder as the script.
3. Run the main script from your terminal:
   python project.py
