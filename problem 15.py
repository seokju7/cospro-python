def solution(stones):
    jump = 0
    count = 0
    while jump < len(stones):
        jump += stones[jump]
        count += 1
    return count


print(solution([2, 5, 1, 3, 2, 1]))