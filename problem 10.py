def solution(data):
    total = sum(data)
    answer = 0
    average = total / len(data)
    for i in data:
        if i <= average:
            answer += 1
    return answer

print(solution([data]))
