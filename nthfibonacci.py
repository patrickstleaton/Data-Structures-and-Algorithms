#O(n) time, O(1) space
# Hold the last two positions within a 2 element array, shifting them out every
# iteration
def getNthFib(n):
    last_two = [0,1]
	counter = 3
	while counter <= n:
		next_fib = last_two[0] + last_two[1]
		last_two[0] = last_two[1]
		last_two[1] = next_fib
		counter +=1
	if n > 1:
		return last_two[1]
	else:
		return last_two[0]