# Ввод элементов массива с клавиатуры
raw = input("Введите элементы массива через пробел: ").strip()

if not raw:
    print("Ошибка: массив не может быть пустым.")
else:
    try:
        arr: list[int] = [int(x) for x in raw.split()]
        k: int = int(input("Введите сдвиг k (>0 вправо, <0 влево): "))

        n: int = len(arr)
        # Приводим сдвиг к диапазону [0, n - 1] без выхода за границы
        shift: int = k % n

        # Выполняем циклический сдвиг с помощью срезов
        if shift == 0:
            shifted: list[int] = arr.copy()
        else:
            shifted = arr[-shift:] + arr[:-shift]

        # Выводим результат
        print("Исходный массив:    ", arr)
        print(f"Сдвиг на k = {k} (фактически вправо на {shift}):")
        print("Массив после сдвига:", shifted)
    except ValueError:
        print("Ошибка: вводите только целые числа.")
