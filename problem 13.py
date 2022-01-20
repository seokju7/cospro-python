def func_a(arr, n):
    new_list = []
    for i in arr:
        if i != n:
            new_list.append(i)
        else:
            continue
    return new_list

def func_b(a, b):
    if a >= b:
        return  a - b
    else:
        return b - a

def func_c(arr):
    maximum = 0
    for i in arr:
        if i > maximum:
            maximum = i
    return maximum

def solution(visitor):
    visitor_2 = func_a(visitor,func_c(visitor))
    max_1 = func_c(visitor)
    max_2 = func_c(visitor_2)
    return func_b(max_1, max_2)

print(solution([10,20,30,40]))