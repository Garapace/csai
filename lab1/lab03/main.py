""" Лаба 1. Git, Python. Создайте файл main.py в директории проекта с программой, которая запрашивает с клавиатуры
n чисел и сортирует их при помощи алгоритма сортировки пузырьком по возрастанию и выводит их на экран. """


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


def main():
    n = int(input("сколько чисел в последовательности?\n"))
    array = [_ for _ in range(n)]
    for i in range(n):
        elem = int(input(f"{i+1}-ый эл-т последовательности - "))
        array[i] = elem
    print(f"начальная последовательность\t\t-\t{' '.join(str(item) for item in array)}")
    print(f"отсортированная последовательность\t-\t{' '.join(str(item) for item in bubble_sort(array))}")


if __name__ == "__main__":
    main()
