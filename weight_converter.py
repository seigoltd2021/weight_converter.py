print("Это конвертер веса")
unit = input("Введите единицы измерения веса (кг, фунты, унции): ")
weight = float(input("Введите вес: "))

if unit == "кг":
    pounds = weight * 2.20462
    ounces = weight * 35.274
    print(weight, "кг =", round(pounds, 2), "фунтов")
    print(weight, "кг =", round(ounces, 2), "унций")
elif unit == "фунты":
    kilograms = weight / 2.20462
    ounces = weight * 16
    print(weight, "фунтов =", round(kilograms, 2), "кг")
    print(weight, "фунтов =", round(ounces, 2), "унций")
elif unit == "унции":
    kilograms = weight / 35.274
    pounds = weight / 16
    print(weight, "унций =", round(kilograms, 2), "кг")
    print(weight, "унций =", round(pounds, 2), "фунтов")
else:
    print("Неверные единицы измерения")
