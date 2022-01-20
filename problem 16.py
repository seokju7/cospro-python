def solution(height, k):
    count = 0
    for i in height:
        if i > k:
            count += 1
    return count


print(solution())