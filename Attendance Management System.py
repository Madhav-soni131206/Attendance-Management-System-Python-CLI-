from datetime import date

attendance = {}



def mark_attendance():
    today = str(date.today())

    if today not in attendance:
        attendance[today] = {}

    print("\n--- Mark Attendance ---")
    n = int(input("Number of students: "))

    for i in range(n):
        name = input(f"Student {i+1} name: ")
        status = input("Present (p) / Absent (a): ").lower()

        if status == "p":
            attendance[today][name] = "Present"
        else:
            attendance[today][name] = "Absent"

    print("Attendance saved!")



def view_attendance():
    if not attendance:
        print("No records yet.")
        return

    print("\n--- Attendance Record ---")

    for d, students in attendance.items():
        print(f"\nDate: {d}")
        for name, status in students.items():
            print(f"{name}: {status}")



def summary():
    total_present = 0
    total_absent = 0

    for day in attendance.values():
        for status in day.values():
            if status == "Present":
                total_present += 1
            else:
                total_absent += 1

    print("\n--- Summary ---")
    print(f"Present: {total_present}")
    print(f"Absent: {total_absent}")

def ai_insights():
    if not attendance:
        print("No data for AI.")
        return

    student_stats = {}


    for day in attendance.values():
        for name, status in day.items():
            if name not in student_stats:
                student_stats[name] = {"present": 0, "total": 0}

            student_stats[name]["total"] += 1
            if status == "Present":
                student_stats[name]["present"] += 1

    print("\n--- AI Insights 🤖 (Local) ---")

    low_attendance = []
    high_attendance = []

    for name, data in student_stats.items():
        percentage = (data["present"] / data["total"]) * 100

        print(f"{name}: {percentage:.1f}% attendance")

        if percentage < 50:
            low_attendance.append(name)
        elif percentage > 80:
            high_attendance.append(name)

    # Suggestions
    print("\n--- Suggestions ---")

    if low_attendance:
        print("⚠️ Students needing attention:")
        for s in low_attendance:
            print(f"- {s}")

    if high_attendance:
        print("⭐ High performing students:")
        for s in high_attendance:
            print(f"- {s}")


    print("\n--- Improvement Tips ---")
    print("- Conduct regular attendance checks")
    print("- Motivate students with low attendance")
    print("- Reward consistent students")
    print("- Communicate with parents if needed")



def main():
    while True:
        print("\n--- Attendance System ---")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Summary")
        print("4. AI Insights 🤖 (Offline)")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            summary()
        elif choice == "4":
            ai_insights()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
