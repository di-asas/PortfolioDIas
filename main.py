import json

class Portfolio:
    def __init__(self, file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def show_about(self):
        print("\n=== О себе ===")
        print(self.data["about"])

    def show_goal(self):
        print("\n=== Моя цель ===")
        print(self.data["goal"])

    def show_it(self):
        print("\n=== Как я пришёл в IT ===")
        print(self.data["it"])

    def show_mentor(self):
        print("\n=== Мой ментор ===")
        print(self.data["mentor"])

    def show_progress(self):
        print("\n=== Точка А → Точка Б ===")
        print(self.data["progress"])

    def show_hobby(self):
        print("\n=== Хобби и интересы ===")
        for hobby in self.data["hobby"]:
            print("-", hobby)

    def show_projects(self):
        print("\n=== Мои лучшие работы ===")
        for project in self.data["projects"]:
            print("-", project)

    def show_github(self):
        print("\n=== GitHub ===")
        print(self.data["github"])


portfolio = Portfolio("data.json")

while True:
    print("""
======== МОЁ ПОРТФОЛИО ========
1. О себе
2. Моя цель
3. Как я пришёл в IT
4. Мой ментор
5. Точка А → Точка Б
6. Хобби и интересы
7. Мои лучшие работы
8. GitHub
0. Выход
===============================
""")

    choice = input("Выберите пункт: ")

    if choice == "1":
        portfolio.show_about()
    elif choice == "2":
        portfolio.show_goal()
    elif choice == "3":
        portfolio.show_it()
    elif choice == "4":
        portfolio.show_mentor()
    elif choice == "5":
        portfolio.show_progress()
    elif choice == "6":
        portfolio.show_hobby()
    elif choice == "7":
        portfolio.show_projects()
    elif choice == "8":
        portfolio.show_github()
    elif choice == "0":
        print("До свидания!")
        break
    else:
        print("Неверный выбор!")
