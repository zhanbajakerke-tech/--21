from django.shortcuts import render

def process(request):
    return render(request, 'students/process.html')

def ratings(request):
    data = load_data()

    rating_list = []
    for student in data["students"]:
        exam1 = data["exam1"].get(student, 0)
        exam2 = data["exam2"].get(student, 0)
        total = int(exam1) + int(exam2)
        rating_list.append({"name": student, "total": total})

    rating_list.sort(key=lambda x: x["total"], reverse=True)

    return render(request, 'students/ratings.html', {"ratings": rating_list})

from django.shortcuts import render, redirect
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "students", "data.json")


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"students": [], "exam1": {}, "exam2": {}}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def process(request):
    return render(request, "students/process.html")


# ------------------- EXAM 1 --------------------
def exam1(request):
    data = load_data()

    if request.method == "POST":
        name = request.POST.get("name")
        score = request.POST.get("score")

        if name and score:
            if name not in data["students"]:
                data["students"].append(name)

            data["exam1"][name] = score
            save_data(data)

        return redirect("exam1")

    return render(request, "students/exam1.html")


# ------------------- EXAM 2 --------------------
def exam2(request):
    data = load_data()

    if request.method == "POST":
        name = request.POST.get("name")
        score = request.POST.get("score")

        if name and score:
            if name not in data["students"]:
                data["students"].append(name)

            data["exam2"][name] = score
            save_data(data)

        return redirect("exam2")

    return render(request, "students/exam2.html")


# ------------------- STUDENT LIST --------------------
def student_list(request):
    data = load_data()

    combined = []
    for student in data["students"]:
        combined.append({
            "name": student,
            "exam1": data["exam1"].get(student, "-"),
            "exam2": data["exam2"].get(student, "-")
        })

    return render(request, "students/student_list.html", {
        "combined": combined})

def ratings(request):
    data = load_data()

    rating_list = []

    for student in data["students"]:
        exam1 = data["exam1"].get(student, 0)
        exam2 = data["exam2"].get(student, 0)

        total = int(exam1) + int(exam2)
        dopusk = total/2
        rating_list.append({
            "name": student,
            "exam1": exam1,
            "exam2": exam2,
            "total": total,
            "dopusk": dopusk
        })

    rating_list.sort(key=lambda x: x["total"], reverse=True)

    return render(request, "students/ratings.html", {
        "ratings": rating_list})
