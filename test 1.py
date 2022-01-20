#1
def solution(price, money):
    answer = 0
    if money >= sum(price):
        answer = money - sum(price)
    else:
        answer = -1
    return answer

#2
def func_a(s):
    s.sort()
    return s[len(s) - 1], s[0]

def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

def solution(scores):
    sum = func_b9(scores)
    max, min = func_a(scores)
    return sum - max - min

#3
def solution(scores):
    count = 0
    for s in range(len(scores)):
        if scores[s] <= 200:
            count += 1
    return count

#4
def solution(price, grade):
    answer = 0
    if grade == 'S':
        answer = int(price * 0.05)
    if grade == 'G':
        answer = int(price * 0.1)
    if grade == 'V':
        answer = int(price * 0.15)
    return answer

#5
def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        while current != 0:
            unit = current % 10
            if unit == 3 or unit == 6 or unit == 9:
                count += 1
            current //= 10
    return count

#6
def solution(left_rings):
    answer = 0
    for i in range(len(left_rings)):
        if left_rings[i] <= i:
            for k in range(i):
                if left_rings[k] >  left_rings[i]:
                    answer += 1
    return answer

#7
def solution(file_info):
    sucess = 0
    fail = 0
    for f in file_info:
        splited = f.split(,)
        if splited[0] == 'jpeg' and splited[2] < 1000:
            sucess += 1
        else:
            fail += 1
    return sucess, fail

#8
def solution(sentence):
    filetered = []
    for s in sentence:
        if s != ' ' and s != '.':
            filetered.append(s)
    before = ''.join(filetered)
    filetered.reverse()
    after = ''.join(filetered)
    return before == after

#9
def solution(characters):
    result = [characters[0]]
    for i in range(1, len(characters)):
        if characters[i - 1] != characters[i]:
            result.append(characters[i])
    return ''.join(result)

#10
def solution(data):
    total = 0
    for i in data:
        total += i
    cnt = 0
    average = total // len(data)
    for i in data:
        if i < average:
            cnt += 1
    return cnt
