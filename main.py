from utils import birinshi_emtihan_engizu, reyting_shygaru, reyting_dopuska

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

# ==== 2-р емтихан ====
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


# ==== Файлмен жұмыс ====
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


# ==== Студент іздеу ====
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


# ==== БАҒДАРЛАМА БАСТАУ ====
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

    n = input("Нұсқаны таңдаңыз (1-8): ")

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
    else:
        print("Қате таңдау! Қайта енгізіңіз.")























