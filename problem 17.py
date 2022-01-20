def solution(s):
    s_lst = list(s)
    for i in range(len(s)):
        if s_lst[i] == 'a':
            s_lst[i] = 'z'
        elif s_lst[i] == 'z':
            s_lst[i] = 'a'
    return ''.join(s_lst)


print(solution('abz'))