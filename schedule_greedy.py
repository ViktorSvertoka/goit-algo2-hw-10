from colorama import Fore, Style, init

# Ініціалізація colorama для Windows
init()


class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        best_teacher = None
        best_coverage = set()

        for teacher in teachers:
            coverage = teacher.can_teach_subjects & remaining_subjects
            if len(coverage) > len(best_coverage) or (
                len(coverage) == len(best_coverage)
                and teacher.age < (best_teacher.age if best_teacher else float("inf"))
            ):
                best_teacher = teacher
                best_coverage = coverage

        if not best_teacher:
            print(
                Fore.RED
                + "Неможливо покрити всі предмети наявними викладачами."
                + Style.RESET_ALL
            )
            return None

        best_teacher.assigned_subjects = best_coverage
        schedule.append(best_teacher)
        remaining_subjects -= best_coverage

    return schedule


if __name__ == "__main__":
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print(Fore.CYAN + "Розклад занять:" + Style.RESET_ALL)
        for teacher in schedule:
            print(
                Fore.GREEN
                + f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
                + Style.RESET_ALL
            )
            print(
                Fore.YELLOW
                + f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n"
                + Style.RESET_ALL
            )
