from utils import birinshi_emtihan_engizu, reyting_shygaru, reyting_dopuska
import numpy as np
import matplotlib.pyplot as plt

print("Студенттердің емтихан нәтижесін басқару жүйесі")

fakultet = "Ақпараттық технологиялар факультеті"
print(f"Факультет: {fakultet}\n")

top_tizimi = ("SIB-21", "SIB-22", "SIB-23")

studentter = {
    "SIB-21": ["Маратова Айзере", "Сарбаев Данияр", "Жақсыбек Самат", "Байжанова Маржан"],
    "SIB-22": ["Сайрамова Мөлдір", "Кенесбаев Нұржан", "Тоқтаров Еркебұлан", "Төлеубеков Темірлан"],
    "SIB-23": ["Оралбай Айбек", "Молдагулова Алия", "Мамыров Ерасыл", "Абдразақ Нұртуған"]
}

baga_zhiyntygy = {}
def ekinshi_emtihan_engizu():
    if not baga_zhiyntygy:
        print("Алдымен 1-р емтихан енгізіңіз!")
        return
    print("\n2-р емтихан нәтижесін енгізіңіз:")
    for at, info in baga_zhiyntygy.items():
        try:
            bal = float(input(f"{at}: "))
        except ValueError:
            print("Қате! Тек сан енгізіңіз.")
            bal = 0
        baga_zhiyntygy[at]["2-емтихан"] = bal
    print("Барлық 2-р емтихан нәтижелері енгізілді.")

def faylga_jazu():
    with open("emtiхан_bagalary.txt", "w", encoding="utf-8") as file:
        for at, info in baga_zhiyntygy.items():
            rub1 = info["1-емтихан"]
            rub2 = info["2-емтихан"] if info["2-емтихан"] is not None else "-"
            file.write(f"{at},{info['топ']},{rub1},{rub2}\n")
    print("Мәліметтер файлға жазылды.")


def fayldan_oku():
    try:
        with open("emtiхан_bagalary.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        for line in lines:
            at, top, rub1, rub2 = line.strip().split(",")
            baga_zhiyntygy[at] = {
                "топ": top,
                "пән": "Белгісіз",
                "1-емтихан": float(rub1),
                "2-емтихан": None if rub2 == "-" else float(rub2)
            }
        print("Файлдан мәліметтер оқылды.")
    except FileNotFoundError:
        print("Файл табылмады, жаңа база жасалады.")


def student_izdeu():
    at = input("Іздейтін студенттің атын енгізіңіз: ").strip().title()
    tabyldy = False
    for esimi, info in baga_zhiyntygy.items():
        if at in esimi:
            rub1 = info["1-емтихан"]
            rub2 = info["2-емтихан"]
            if rub2 is not None:
                ort = (rub1 + rub2) / 2
                dopusk = "бар" if ort >= 50 else "жоқ"
                print(f"{esimi}: {rub1}, {rub2} → орташа {ort:.1f}, допуск {dopusk}")
            else:
                print(f"{esimi}: тек 1-р емтихан бар ({rub1})")
            tabyldy = True
    if not tabyldy:
        print("Мұндай студент табылмады.")


class StudentInfo:
    def init(self, name, top, rub1, rub2=None):
        self.name = name
        self.top = top
        self.rub1 = rub1
        self.rub2 = rub2

    def orta(self):
        if self.rub2 is None:
            return self.rub1
        return (self.rub1 + self.rub2) / 2

    def info(self):
        return f"{self.name} ({self.top}) – 1-р: {self.rub1}, 2-р: {self.rub2}, орташа: {self.orta():.1f}"


class TopStudent(StudentInfo):
    def init(self, name, top, rub1, rub2=None, bonus=5):
        super().init(name, top, rub1, rub2)
        self.bonus = bonus

    def orta(self):
        return super().orta() + self.bonus


def oop_studentter_tizimi():
    print("\n OOP үлгісі: StudentInfo және TopStudent")
    for at, info in baga_zhiyntygy.items():
        if "А" in at:
            st = TopStudent(at, info["топ"], info["1-емтихан"], info["2-емтихан"])
        else:
            st = StudentInfo(at, info["топ"], info["1-емтихан"], info["2-емтихан"])
        print(st.info())


def grafik_orta_bagalar():
    if not baga_zhiyntygy:
        print("Алдымен емтихан мәліметтерін енгізіңіз!")
        return

    atar = []
    ortalar = []

    for at, info in baga_zhiyntygy.items():
        rub1 = info["1-емтихан"]
        rub2 = info["2-емтихан"] if info["2-емтихан"] else 0
        ort = np.mean([rub1, rub2])
        atar.append(at)
        ortalar.append(ort)

    ortalar_np = np.array(ortalar)
    print("\nСтуденттердің орташа балдары (NumPy):")
    print(ortalar_np)

    plt.figure(figsize=(10, 5))
    plt.plot(atar, ortalar_np, marker="o")
    plt.xticks(rotation=45)
    plt.title("Студенттердің орташа балдар динамикасы")
    plt.ylabel("Балл")
    plt.grid()
    plt.tight_layout()
    plt.show()



fayldan_oku()



while True:
    print("\n📘 Мәзір:")
    print("1. 1-р емтихан нәтижесін енгізу (utils.py)")
    print("2. 2-р емтихан нәтижесін енгізу")
    print("3. Топтық орташа рейтинг (utils.py)")
    print("4. Жеке рейтинг және допуск (utils.py)")
    print("5. Студент іздеу")
    print("6. Мәліметтерді файлға сақтау")
    print("7. Файлдағы барлық мәліметтерді көру")
    print("8. Шығу")
    print("9. OOP – класс арқылы студенттерді шығару")
    print("10. NumPy және Matplotlib – бағалар графигі")

    n = input("Нұсқаны таңдаңыз (1-10): ")

    if n == "1":
        baga_zhiyntygy = birinshi_emtihan_engizu(studentter, baga_zhiyntygy)
    elif n == "2":
        ekinshi_emtihan_engizu()
    elif n == "3":
        reyting_shygaru(baga_zhiyntygy, top_tizimi)
    elif n == "4":
        reyting_dopuska(baga_zhiyntygy)
    elif n == "5":
        student_izdeu()
    elif n == "6":
        faylga_jazu()
    elif n == "7":
        print("\nФайлдағы барлық мәліметтер:")
        for at, info in baga_zhiyntygy.items():
            print(at, ":", info)
    elif n == "8":
        print("Бағдарлама аяқталды. Сәттілік!")
        break
    elif n == "9":
        oop_studentter_tizimi()
    elif n == "10":
        grafik_orta_bagalar()
    else:
        print("Қате таңдау! Қайта енгізіңіз.")




















