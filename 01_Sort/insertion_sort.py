def insertion_sort(l: list):
    """
    주어진 리스트를 삽입 정렬 알고리즘을 이용하여 정렬합니다.
    1차원 배열에 대해서만 적용됩니다.

    Args:
        l (list): 정렬할 데이터가 담긴 리스트

    Returns:
        l (list): 정렬된 리스트
    """

    for i in range(1, len(l)):
        target_val = l[i]
        j = i - 1
        while j >= 0 and l[j] > target_val:
            l[j + 1] = l[j]
            j = j - 1
            # print(l) # 정렬 과정 확인

        l[j + 1] = target_val
        # print(l) # 정렬 과정 확인

    return l

x = [7, 3, 5, 0, 6, 1, 4, 8, 2, 9]
x_sorted = insertion_sort(x)

print(x_sorted)
