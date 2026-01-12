def bubble_sort(l: list):
    """
    주어진 리스트를 버블 정렬 알고리즘을 이용하여 정렬합니다.
    1차원 배열에 대해서만 적용됩니다.

    Args:
        l (list): 정렬할 데이터가 담긴 리스트

    Returns:
        l (list): 정렬된 리스트
    """

    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

        # print(l) # 정렬 과정 확인
    
    return l

x = [7, 3, 5, 0, 6, 1, 4, 8, 2, 9]
x_sorted = bubble_sort(x)

print(x_sorted)
