def decimal_to_binary(n):
    if n < 0:
        return '-' + bin(abs(n))[2:]
    return bin(n)[2:]

def decimal_to_octal(n):
    if n < 0:
        return '-' + oct(abs(n))[2:]
    return oct(n)[2:]

try:
    # Получаем число от пользователя
    decimal_number = int(input("Введите десятичное число: "))

    # Переводим в двоичную и восьмеричную системы
    binary_number = decimal_to_binary(decimal_number)
    octal_number = decimal_to_octal(decimal_number)

    # Выводим результаты
    print(f"Двоичное представление: {binary_number}")
    print(f"Восьмеричное представление: {octal_number}")

except ValueError:
    print("Ошибка: Вы ввели недопустимый символ. Пожалуйста, введите целое десятичное число.")
