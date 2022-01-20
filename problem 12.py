def soluion(scores):
    answer = sum(scores) - max(scores) - min(scores)
    return answer


print(soluion([50, 90, 65, 100]))