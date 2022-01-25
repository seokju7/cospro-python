#1

def solution(n,price):
    games = (n * n) // 2
    per_day = n // 2
    answer = (games // per_day) * price
    return answer

#2

def solution(shoes_size):
    answer = [0 for _ in range(6)]
    size_list = ['7', '7.5', '8', '8.5', '9', '9.5']
    for i in shoes_size:
        if i == size_list[0]:
            answer[0] += 1
        if i == size_list[1]:
            answer[1] += 1
        if i == size_list[2]:
            answer[2] += 1
        if i == size_list[3]:
            answer[3] += 1
        if i == size_list[4]:
            answer[4] += 1
        if i == size_list[5]:
            answer[5] += 1
    return answer

#3

def func_a(arr, num):
    ret = []
    for i in arr:
        if (i != num):
            ret.append(i)
    return ret

def func_b(a, b):
    if a> b:
        return a - b
    else:
        return b - a

def func_c(arr):
    ret = -1
    for i in arr:
        if ret< i:
            ret = i
    return ret

def solution(visitor):
    max_first = func_c(visitor)
    visitor_removed = func_a(visitor, max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first, max_second)
    return answer

#4

def solution(scores):
    grade_counter = [o for i in range(5)]
    for i in scores:
        if i >= 85:
            grade_counter[0] += 1
        elif i >= 70:
            grade_counter[1] += 1
        elif i >= 55:
            grade_counter[2] += 1
        elif i >= 40
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter

#5

def func_a(arr):
    counter = [0 for _ in range(1001)]
    for i in arr:
        counter[i] += 1
    return counter

def func_b(arr):
    ret = 0
    for i in arr:
        if ret < i:
            ret = i
    return ret

def func_c(arr):
    ret = func_b(arr)
    for i in arr:
        if ret > i:
            ret = i
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_c(counter)
    min_cnt = func_b(counter)
    return max_cnt // min_cnt

#6

def solution(weight, k):
    answer = 0
    for w in weight:
        if w > k:
            answer += 1
    return answer   

#7

def solution(s):
    answer = []
    for c in s:
        if '0' <= c <= '9':
            n = ord(i)-ord(c)
            c = chr(n)
        answer.append(c)
    return ''.join(answer)

#8

def solution(name_list):
    answer = 0
    for name in name_list:
        for char in name:
            if char == 'A' or char == 'k':
                answer += 1
                break
    return answer

#9

def solution(orders):
    answer = 0
    size = 0
    for o in orders:
        for i in range(6):
            if o[i] != 0:
                size += ((i + 1) ** 2) * o[i]
    answer = size // 36
    if size % 36 != 0:
        answer += 1
    return answer

#10

def sum_isbn(isbn):
    sum = 0
    for i in range(len(isbn)):
        c = int(isbn[i])
        if i % 2:
            w = 3
        else:
            w = 1
        sum += w * c
    return sum

def solution(isbn):
    answer = ''
    lef = (sum_isbn(isbn) - int(isbn[12])) % 10
    answer = (10 - lef - int(isbn[12]))
    if answer == 10:
        answer = 0
    return answer
