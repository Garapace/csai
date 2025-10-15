import matplotlib.pyplot as plt

def fibonacci(n):
    fib_numbers = [0, 1]  # Инициализируем первые два числа Фибоначчи
    for i in range(2, n):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
    return fib_numbers

# Параметр N - количество чисел Фибоначчи для вычисления
N = 25
fib_numbers = fibonacci(N)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(range(N), fib_numbers, marker='o', color='b', linestyle='-')
plt.title(f'Первые {N} чисел Фибоначчи')
plt.xlabel('Номер числа Фибоначчи')
plt.ylabel('Величина числа Фибоначчи')
plt.grid(True)
plt.show()
