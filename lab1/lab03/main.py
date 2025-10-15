""" Лаба 1. Git, Python. Создайте файл main.py в директории проекта с программой, которая запрашивает с клавиатуры
n чисел и сортирует их при помощи алгоритма сортировки пузырьком по возрастанию и выводит их на экран. """


def bubble_sort(array, direction):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if direction == 0:  # по возрастанию
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            else:               # по убыванию
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    return array


def main():
    n = int(input("сколько чисел в последовательности?\n"))
    array = [int(input(f"{i+1}-ый элемент: ")) for i in range(n)]
    
    direction = int(input("Введите направление сортировки:\n0 - по возрастанию | 1 - по убыванию\n"))
    print(f"начальная последовательность\t\t-\t{' '.join(str(item) for item in array)}")
    print(f"отсортированная последовательность\t-\t{' '.join(str(item) for item in bubble_sort(array, direction))}")


if __name__ == "__main__":
    main()
