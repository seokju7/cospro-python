def solution(scores):
    score_list = [0,0,0,0,0]
    for i in scores:
        if 85<= i <101:
            score_list[0] += 1
        if 70<= i <85:
            score_list[1] += 1
        if 55<= i <70:
            score_list[2] += 1
        if 40<= i <55:
            score_list[3] += 1
        if 0<= i <40:
            score_list[4] += 1
    return score_list



print(solution([100,70,55,40,0]))