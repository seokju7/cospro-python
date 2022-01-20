# P4
arr = [1,2,3,3,1,3,3,2,3,2]
def solution(arr):
    counter = {}
    for i in arr:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1
    keys = list(counter.keys())
    count_max = counter.get(max(keys))
    count_min = counter.get(min(keys))
    answer = (count_max // count_min)
    return answer

print(solution(arr))
