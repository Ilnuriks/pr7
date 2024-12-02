def decimal_to_nine(n):
    if n == 0:
        return "0"
    n = abs(n)
    result = ""
    while n > 0:
        result = str(n % 9) + result
        n //= 9
    if n < 0:
        result = "-" + result
    return result

try:
    # Получаем число от пользователя
    decimal_number = int(input("Введите десятичное число: "))

    # Переводим в девятеричную систему
    nine_number = decimal_to_nine(decimal_number)

    # Выводим результат
    print(f"Девятеричное представление: {nine_number}")

except ValueError:
    print("Ошибка: Вы ввели недопустимый символ. Пожалуйста, введите целое десятичное число.")
