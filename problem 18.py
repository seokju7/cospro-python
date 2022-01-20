def solution(name_list)
    cnt = 0
    for name in name_list
        index = 0
        for _ in range(len(name))
            if name[index] == 'j' or name[index] ==  'k'
                cnt += 1
                break
            index += 1

    return cnt


print(solution(['james', 'jack', 'amy']))




























