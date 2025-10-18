print("=== Онлайн тест нәтижелерінің орташа ұпайларын талдау жүйесі ===")

test_atauy = "Python тесті"
max_bal = 100

# Алғашқы студенттерді енгізу
natizheler = {}
sany = int(input("Неше студент енгізгіңіз келеді (мысалы 3): "))
for i in range(sany):
    aty = input(str(i+1) + "-студенттің аты: ")
    bal = int(input("Ұпайы: "))
    natizheler[aty] = bal

print("\nЕнгізілген студенттер мен ұпайлар:")
for a, b in natizheler.items():
    print(a, ":", b)

# Орташа балл есептеу
ortasha = sum(natizheler.values()) / len(natizheler)
print("\nОрташа ұпай:", round(ortasha, 1))

# Қайталанатын мәндерді тексеру
unik = set(natizheler.values())
print("Бірегей ұпайлар:", unik)

# Студент іздеу
izdeu = input("\nІзделетін студенттің атын енгізіңіз: ").lower()
bar = False
for a in natizheler.keys():
    if izdeu == a.lower():
        print(a, "табылды, ұпайы:", natizheler[a])
        bar = True
        break
if not bar:
    print("Студент табылмады.")

# Сайт картасы арқылы жалғастыру
while True:
    print("\n=== Сайт картасы ===")
    print("1. Студент қосу\n2. Нәтижелерді көру\n3. Шығу")
    t = input("Таңдау: ")

    if t == "1":
        a = input("Аты: ")
        b = int(input("Ұпай: "))
        natizheler[a] = b
        print("Қосылды!")
    elif t == "2":
        print("\nБарлық нәтижелер:")
        for a, b in natizheler.items():
            print(a, ":", b)
        print("Орташа ұпай:", round(sum(natizheler.values()) / len(natizheler), 1))
    elif t == "3":
        print("Бағдарлама аяқталды")
        break
    else:
        print("Қате енгізу!")





















