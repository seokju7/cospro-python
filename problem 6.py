def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count
        while current != 0:
            x = current % 10
            if x == 3 or x == 6 or x == 9:
                count +=1
                print('짝', end = '')
            current = current // 10
        if temp == count:
            print(i, end='')
        print('',end=' ')
    print('')
    return count

print(solution(40))
