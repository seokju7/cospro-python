# P2
def solution(price,grade):

if grade == 'S':
	answer = int(price*0.95)
if grade == 'G':
	answer = int(price*0.9)
if grade == 'V':
	answer = int(price*0.85)

return answer