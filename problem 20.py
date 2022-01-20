def solution(arr ,k):
    answer = 0
    lst = []
    for x in arr:
        for y in x:
            lst.append(y)
    lst.sort()
    answer = lst[k - 1]
    return answer


print(solution([[5,12,4,31],
                [24,13,11,2],
                [43,44,19,26],
                [33,65,20,21]], 4))
