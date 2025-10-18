print("Студенттердің емтихан бағасының рейтингін шығару жүйесі")


fakultet_atauy = "Ақпараттық технологиялар факультеті"
print(f"Факультет: {fakultet_atauy}\n")


top_tizimi = ("SIB-21", "SIB-22", "SIB-23")


studentter = {
    "SIB-21": ["Маратова Айзере", "Сарбаев Данияр", "Жақсыбек Самат", "Байжанова Маржан"],
    "SIB-22": ["Сайрамова Мөлдір", "Кенесбаев Нұржан", "Тоқтаров Еркебұлан", "Төлеубеков Темірлан"],
    "SIB-23": ["Оралбай Айбек", "Молдагулова Алия", "Мамыров Ерасыл", "Абдразақ Нұртуған"]
}


baga_zhiyntygy = {}


pan_atauy = input("Пән атауын енгізіңіз: ").strip().title()


for top, tizim in studentter.items():
    print(f"\n{top} тобының студенттері үшін емтихан балы енгізіңіз:")
    for at in tizim:
        bal = float(input(f"{at}: "))
        baga_zhiyntygy[at] = {"топ": top, "пән": pan_atauy, "бал": bal}


print("\nӘр топтың рейтингі")
for top in top_tizimi:
    toplam = 0
    san = 0
    for at, info in baga_zhiyntygy.items():
        if info["топ"] == top:
            toplam += info["бал"]
            san += 1
    if san > 0:
        ort_baga = toplam / san
        print(f"{top} тобының рейтингі: {round(ort_baga, 2)}")


while True:
    print("\nСайт картасы")
    print("1. Барлық бағаларды көру")
    print("2. Студентті іздеу")
    print("3. Жүйеден шығу")
    tandau = input("Нұсқаны таңдаңыз (1/2/3): ")
    
    if tandau == "1":
        for at, info in baga_zhiyntygy.items():
            print(f"{at} — {info['топ']}, пәні: {info['пән']}, емтихан балы: {info['бал']}")
    elif tandau == "2":
        izdelgen_at = input("Іздейтін студенттің атын енгізіңіз: ").strip().title()
        tabyldy_ma = False
        for at, info in baga_zhiyntygy.items():
            if izdelgen_at.lower() in at.lower():
                print(f"{izdelgen_at} {info['топ']} тобында оқиды, пәні: {info['пән']}, емтихан балы: {info['бал']}")
                tabyldy_ma = True
                break
        if not tabyldy_ma:
            print(f"{izdelgen_at} студенті базадан табылмады.")
    elif tandau == "3":
        print("Бағдарлама аяқталды. Сәттілік тілейміз!")
        break
    else:
        print("Қате таңдау, қайта көріңіз.")
























