def birinshi_emtihan_engizu(studentter, baga_zhiyntygy):
    pan = input("Пән атауын енгізіңіз: ").strip().title()
    print(f"\n{pan} пәні бойынша 1-р емтихан нәтижесін енгізіңіз:")

    for top, tizim in studentter.items():
        print(f"\n{top} тобының студенттері:")
        for at in tizim:
            try:
                bal = float(input(f"{at}: "))
            except ValueError:
                print("Қате! Тек сан енгізіңіз.")
                bal = 0
            baga_zhiyntygy[at] = {"топ": top, "пән": pan, "1-емтихан": bal, "2-емтихан": None}
    return baga_zhiyntygy


def reyting_shygaru(baga_zhiyntygy, top_tizimi):
    print("\nТоптар бойынша орташа рейтинг:")
    for top in top_tizimi:
        kos = 0
        san = 0
        for at, info in baga_zhiyntygy.items():
            if info["топ"] == top:
                if info["1-емтихан"] is not None and info["2-емтихан"] is not None:
                    ort = (info["1-емтихан"] + info["2-емтихан"]) / 2
                    kos += ort
                    san += 1
        if san > 0:
            print(f"{top} тобының орташа балы: {round(kos / san, 2)}")
        else:
            print(f"{top} тобының дерегі жоқ.")


def reyting_dopuska(baga_zhiyntygy):
    print("\nЖеке рейтинг және сессияға допуск:")
    for at, info in baga_zhiyntygy.items():
        rub1 = info["1-емтихан"]
        rub2 = info["2-емтихан"]
        if rub2 is None:
            print(f"{at} — 2-р емтихан бағасы енгізілмеген.")
        else:
            ort = (rub1 + rub2) / 2
            if ort >= 50:
                print(f"{at} ({info['топ']}) орташа балл {ort:.1f}  Допуск бар")
            else:
                print(f"{at} ({info['топ']}) орташа балл {ort:.1f}  Допуск жоқ")
