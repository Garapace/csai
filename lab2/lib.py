def fibonacci(n):
    fib_numbers = [0, 1]  # Инициализируем первые два числа Фибоначчи
    for i in range(2, n):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
    return fib_numbers[:n]  # Возвращаем только первые n элементов


def bubble_sort(arr):
    sorted_arr = arr.copy()  # Создаем копию исходного списка
    n = len(sorted_arr)

    # Выполняем сортировку пузырьком
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Меняем местами, если предыдущий элемент больше следующего
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    return sorted_arr

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Ошибка: неверный оператор"
