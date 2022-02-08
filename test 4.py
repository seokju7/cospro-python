#1

def soluton(cards):
    answer = 0
    for i in range(3):
        for k in range(i, 5):
            for m in range(k, 5):
                if (cards[i] + cards[k] + cards[m]) % 2 == 1:
                    answer += 1
    return answer

#2

def func_a(arr):
    total = 0
    for i in arr:
        total += i
    return total


def solution(arr, payload):
    answer = 0
    sum = func_a(arr)
    if sum >= payload:
        arr.pop()
        arr.reverse()
        weight = 0
        for i in range(len(arr)):
            diff = payload - weight
            if arr[i] <= diff:
                weight += arr[i]
                answer += 1
        if weight != payload:
            answer = 0
    return answer

#3

def solution(student, apts):
    result = 0
    sum_st = int(sum(student))
    if sum_st % 12 != 0:
        result = (sum_st // 12) + 1
    else
        result = sum_st // 12
    return result

#4

def solution(n,m):
    answer = 0
    OPEN, CLOSE = 0, 1
    room = [CLOSE for i in range(m)]
    for i in range(1, n + 1):
        for k in range(1, m + 1):
            if k % i == 0:
                room[k] = OPEN
    answer = room.count(0)
    return answer

#5

def func_a(s):
    answer = 0
    cnt = 0
    for i in s:
        if i == '[':
            cnt += 1
        if i == ']':
            cnt -= 1
    if cnt == 0:
        answer = 1
    return answer

def solution(string):
    answer = 0
    if not func_a(string):
        return -1
    for i in string:
        if i == ']':
            answer += 1
    return answer

#6

def solution(arr):
    answer = [0 for i in range(3)]
    for i in range(3):
        for k in range(4):
            answer[i] += arr[i + 1]
    return answer

#7

def solution(input):
    answer = 0
    x = 0
    y = 0
    for i in input:
        if i == 'w':
            y -= 1
        elif i == 's':
            y += 1
        elif i == 'a':
            x -= 1
        elif i == 'd':
            x += 1
        if x == y: answer += 1
    return answer

#8

def func_a(a):
    total = 0
    for i in a:
        total += i
    return total


def func_b(a, b):
    return a - b if a < b else b - a

def func_c(a, b):
    max_diff = 0
    max_score = 0
    for i in b:
        diff = func_b(a, i)
        if max_diff > diff:
            max_diff = diff
            max_score = i
    return max_score

def solution(scores):
    total = func_a(scores)
    avg = total // len(scores)
    answer = func_c(avg, scores)
    return answer

#9

def solution(arr, k):
    answer = 0
    for i in arr:
        answer //= k
        if i % k != 0
            answer += 1
    return answer

#10

def solution(positive, negative):
    answer = [0,0]
    total_pos = 0
    total_neg = 0
    for i in positive:
        total_pos += sum(i)
    for i in negative:
        total_neg += sum(i)
    total = total_pos + total_neg
    answer[0] = int((total_pos / total) * 100)
    answer[1] = int((total_neg / total) * 100)
    return answer
