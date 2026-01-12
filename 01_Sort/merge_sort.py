def merge_sort(l: list):
    """
    주어진 데이터를 병합 정렬 알고리즘을 이용하여 정렬합니다.
    1차원 배열에 대해서만 적용됩니다.

    Args:
        l (list): 정렬할 데이터가 담긴 리스트

    Returns:
        l (list): 정렬된 리스트
    """

    if len(l) > 1:
        mid = len(l) // 2

        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])

        result = []
        a, b = 0, 0
        while a < len(left) and b < len(right):
            if left[a] > right[b]:
                result.append(right[b])
                b = b + 1
            else:
                result.append(left[a])
                a = a + 1
        if a < len(left):
            result = result + left[a:]
        else:
            result = result + right[b:]

        return result

    else:
        return l

x = [7, 3, 5, 0, 6, 1, 4, 8, 2, 9]
x_sorted = merge_sort(x)

print(x_sorted)
