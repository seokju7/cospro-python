def func_a(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def solution(n, m):
    answer = func_a(m) - func_a(n - 1)
    return answer

print(solution(n, m))