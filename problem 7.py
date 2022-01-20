def solution(scores):
    count = 0
    for score in scores:
        if score >= 650 and score < 800:
            count += 1
    return count

scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
print(solution(scores))
