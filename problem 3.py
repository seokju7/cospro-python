# P3
def func_a(month, day):

	monthrange = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	total  = 0
	for i in range(month - 1):
		total += monthrange[i]
	total += day
	retrun total - 1

def solution(start_m, start_d, end_m, end_d ):
	start = func_a(start_m, start_d)
	end = func_a(end_m, end_d)
	answer = end - start

	return answer