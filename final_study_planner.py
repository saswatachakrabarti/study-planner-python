class Subject:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

    def display(self):
        print(f"Subject: {self.name}, Difficulty: {self.difficulty}")

class StudyPlan:
    def __init__(self):
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def total_difficulty(self):
        total = 0
        for sub in self.subjects:
            total += sub.difficulty
        return total

    def get_subjects(self):
        return self.subjects

class TimeTableGenerator:
    def __init__(self, study_plan):
        self.study_plan = study_plan

    def create_timetable(self, total_hours, days):
        timetable = []
        subjects = self.study_plan.get_subjects()
        total_difficulty = self.study_plan.total_difficulty()

        if total_difficulty == 0:
            return timetable

        subject_hours = {}
        for sub in subjects:
            hours = (sub.difficulty / total_difficulty) * total_hours
            subject_hours[sub.name] = hours

        for day in range(1, days + 1):
            day_plan = {}
            for sub in subjects:
                hours_for_day = subject_hours[sub.name] / days
                day_plan[sub.name] = round(hours_for_day, 2)
            timetable.append(day_plan)

        return timetable

def display_menu():
    print("\n------ Study Planner Menu ------")
    print("1. Add a Subject")
    print("2. View Subjects")
    print("3. Generate Timetable")
    print("4. Exit")

def main():
    study_plan = StudyPlan()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter subject name: ")
            difficulty = int(input("Enter difficulty (1-5): "))
            new_subject = Subject(name, difficulty)
            study_plan.add_subject(new_subject)
            print("Subject added!")

        elif choice == "2":
            subjects = study_plan.get_subjects()
            if len(subjects) == 0:
                print("No subjects added!")
            else:
                print("\nSubjects:")
                for s in subjects:
                    s.display()

        elif choice == "3":
            if len(study_plan.get_subjects()) == 0:
                print("Add subjects first!")
            else:
                total_hours = float(input("Enter total study hours per day: "))
                days = int(input("Days to plan: "))
                generator = TimeTableGenerator(study_plan)
                timetable = generator.create_timetable(total_hours, days)

                print("\n--- Timetable ---")
                for i, day_plan in enumerate(timetable, start=1):
                    print(f"\nDay {i}:")
                    for subject, hours in day_plan.items():
                        print(f"{subject}: {hours} hrs")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
