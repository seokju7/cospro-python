#5
arr = [1, 4, 2, 3]

def solution(arr):
    answer = []
    right = len(arr) - 1

    for i in arr:
        answer.append(arr[right])
        right -= 1

    return answer


# def solution(arr):
#     left, right = 0, len(arr) - 1
# 
#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
# 
#         left += 1
#         right -= 1
# 
#     return arr

if __name__ == '__main__':
    print(solution(arr))

