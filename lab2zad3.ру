# Вводим номер месяца с клавиатуры
try:
    month: int = int(input("Введите номер месяца (1–12): "))

    # Проверяем, попадает ли число в допустимый диапазон
    if month < 1 or month > 12:
        print("Ошибка: номер месяца должен быть от 1 до 12.")
    else:
        # Определяем время года с помощью сложных логических условий
        if month == 12 or month == 1 or month == 2:
            season: str = "Зима"
        elif 3 <= month <= 5:
            season = "Весна"
        elif 6 <= month <= 8:
            season = "Лето"
        else:
            season = "Осень"

        # Определяем количество дней в месяце
        if month == 2:
            days: str = "28 (29 в високосный год)"
        elif month in (4, 6, 9, 11):
            days = "30"
        else:
            days = "31"

        # Выводим результат с пояснениями
        print(f"Месяц №{month}: время года — {season}, дней — {days}.")
except ValueError:
    print("Ошибка: введите целое число.")
