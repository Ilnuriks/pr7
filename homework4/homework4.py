try:
    # Ввод значений a, b и c
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))

    # Проверка на деление на ноль
    if b == 0:
        print("Ошибка: Деление на ноль недопустимо.")
    else:
        # Вычисление x
        x = a / b + c * a
        # Вывод результата
        print(f"Решение уравнения: x = {x}")

except ValueError:
    print("Ошибка: Пожалуйста, введите числовые значения для a, b и c.")