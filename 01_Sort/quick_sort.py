def quick_sort(l: list):
    """
    주어진 리스트를 퀵 정렬 알고리즘을 이용하여 정렬합니다.
    1차원 배열에 대해서만 적용됩니다.

    Args:
        l (list): 정렬할 데이터가 담긴 리스트

    Returns:
        l (list): 정렬된 리스트
    """

    if len(l) > 1:
        mid = len(l) // 2
        pivot = l[mid]

        l[mid], l[-1] = l[-1], l[mid]

        head = 0
        tail = len(l) - 2
        while True:
            while head <= tail and l[head] < pivot:
                head = head + 1
            
            while head <= tail and l[tail] > pivot:
                tail = tail - 1

            # print(l) # 정렬 과정 확인
            
            if head < tail:
                l[head], l[tail] = l[tail], l[head]
                head = head + 1
                tail = tail - 1
            else:
                l[head], l[-1] = l[-1], l[head]
                break

        left = quick_sort(l[:head])
        right = quick_sort(l[head + 1:])

        return left + [pivot] + right

    else:
        return l
    
x = [7, 3, 5, 0, 6, 1, 4, 8, 2, 9]
x_sorted = quick_sort(x)

print(x_sorted)
