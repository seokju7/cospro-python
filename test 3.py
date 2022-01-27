#1
def solution(a,b):
    answer = 0
    diff = a - b
    answer = 10 / diff
    return answer * 60

#2
def func_a(arr):
    total = 0
    for i in arr:
        total += i
    return total


def solution(total, arr):
    result = []
    req_total = func_a(arr)
    for i in arr:
        if req_total > total:
            result.append(total / len(arr))
        else:
            result.append(i)
    return result

#3
def solution(table):
    answer = 0
    st_cnt = [0 for _ in range(6)]
    for grade in range(5):
        for student in range(1,5):
            if table[0][grade] == table[student][grade]:
                st_cnt[student] += 1
    answer = st_cnt.index(max(st_cnt))
    return answer

#4
def solution(walls):
    answer = 0
    painted_walls = 0
    hour = 1
    while painted_walls < walls:
        painted_walls = (hour) + (hour / 2) + (hour / 4)
        hour += 1
    answer = hour
    return answer

#5
def solution(mho_cards, mhe_cards):
    result = -1
    for i in range(13):
        if mho_cards[i] > mhe_cards[i]:
            result += 1
        if mhe_cards[i] < mhe_cards[i]:
            result -= 1
    if result >= 0:
        result  = 1
    if result < -1:
        result = 0     
    return result

#6
def solution(string):
    answer = 0
    number = 0
    s = string + ' '
    for c in s:
        if c.isnumeric() and c == c:
            number = (number * 10) + int(c)
        else:
            answer += number
            number = 0
    return answer

#7
def solution(a,b):
    result = [0,0]
    for i in range(3):
        temp = b
        for k in range(3):
            if a % 10 == temp % 10:
                if i == k:
                    result[0] += 1
                else:
                    result[1] += 1
            temp //= 10
        a //= 10
    return result

#8
def solution(password, key):
    answer = 0
    match_cnt = 0
    for k in key:
        for p in password:
            if k == p:
                match_cnt += 1
                break
    if match_cnt >= len(key):
        answer = 1
    return answer
s
#9
def solution(scores):
    result = [0,0,0,0]
    for i in range(4):
        for k in range(4):
            if i != k:
                result[i] += 2
    return result

#10
def solution(strings):
    result = 0
    for s in strings:
        length = len(s)
        result += (length // 4)
        if length % 4 == 0:
            result += 1
    return result
