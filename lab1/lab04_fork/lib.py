def common_elements_count(*lists):
    if not lists:
        return 0

    common_list = set(lists[0])
    for LIST in lists[1:]:
        common_list &= set(LIST)

    return len(common_list)


arr1 = [1, 5, 3, 7, 8]
arr2 = [2, 5, 6, 7, 8]
arr3 = [0, 5, 9, 7, 8]
print(f"кол-во одинаковых элементов в списках - {common_elements_count(arr1, arr2, arr3)}")
