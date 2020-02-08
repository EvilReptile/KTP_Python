groupmates = [
    {
        "name":"Александр",
        "surname":"Иванов",
        "exams":["АиГ", " ЭЭиСЭ", "Веб"],
        "marks":[4, 3, 5]
    },
    {
        "name":"Иван",
        "surname":"Петров",
        "exams":["История", "АиГ", "КТП"],
        "marks":[4, 4, 4]
    },
    {
        "name":"Кирилл",
        "surname":"Смирнов",
        "exams":["Философия", "ИС", "КТП"],
        "marks":[5, 5, 5]
    },
    {
        "name":"Семен",
        "surname":"Антипов",
        "exams":["ФП", "СиАОД", "Информатика"],
        "marks":[5, 3, 5]
    },
    {
        "name":"Егор",
        "surname":"Перов",
        "exams":["Информатика", "ВТ", "ТЯП"],
        "marks":[5, 5, 4]
    }
]

def print_students(students):
    print(u"Введите средний балл для фильтрации")
    average_mark = float(input())
    
    print(u"Имя".ljust(15), u"Фамилия".ljust(15), u"Экзамены".ljust(30),
          u"Оценки".ljust(20))

    for student in students:
        if sum(student["marks"])/len(student["marks"]) > average_mark:
            print(student["name"].ljust(15), student["surname"].ljust(15),
               str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

print_students(groupmates)
