📘 Attendance Management System (Python CLI)

📌 Overview

This is a basic command-line attendance management system developed using Python. It allows users to mark attendance, view records, generate summaries, and get simple AI-based insights about student attendance.

🚀 Features

✅ Mark attendance (Present/Absent)

📊 View attendance records by date

📈 Generate overall summary (total present & absent)

🤖 AI Insights (offline analysis of attendance patterns)

🖥️ Simple menu-driven interface



🛠️ Technologies Used

Python (Beginner level)

Built-in libraries:

datetime (for date tracking)


📂 How It Works

Attendance is stored in a dictionary with date as the key

Each date contains student names and their attendance status

Data is stored temporarily (not saved to a file)


▶️ How to Run

Make sure Python is installed

Save the code in a file, e.g., attendance.py

Open terminal / command prompt

Run the program:

python attendance.py


📋 Menu Options

Mark Attendance

Enter number of students

Input names and mark Present (p) or Absent (a)

View Attendance

Displays attendance records date-wise


Summary

Shows total present and absent count

AI Insights 🤖 (Offline)

Calculates attendance percentage


Identifies:

Low attendance students (<50%)

High attendance students (>80%)

Provides improvement suggestions

Exit

Closes the program


🤖 About AI Insights

The AI feature in this project is rule-based, not a real machine learning model. It analyzes attendance data and provides insights based on predefined conditions.


⚠️ Limitations

❌ Data is not saved permanently (resets after program ends)

❌ No graphical interface (CLI only)

❌ No error handling for invalid inputs

🔮 Future Improvements

Add file storage (CSV/Database)

Create a GUI version

Integrate real AI/ML models

Add student login system
 
 
 
 Author : Madhav Soni ( 25BCE11351)
