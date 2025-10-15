""" Создайте файл lib.py в директории проекта с функцией,
которая принимает на вход N списков и возвращает количество одинаковых элементов в них """


def common_elements_count(*lists):
    if not lists:
        return 0

    common_list = set(lists[0])     # преобразуем первый список в множество
    for LIST in lists[1:]:          # для каждого следующего списка
        common_list &= set(LIST)    # находим пересечение (общие элементы)
 
    return len(common_list)


def main():
    array1 = [1, 2, 3, 90, 45, 6, 12, 52]
    array2 = [1, 123, 3, 90, 132, 6, 52]
    array3 = [1, 123, 3, 90, 132, 6, 52, 123, 4, 345]
    print(f"кол-во одинаковых элементов в списках - {common_elements_count(array1, array2, array3)}")


if __name__ == "__main__":
    main()
