# Traverse the array and recursively traverse each nested array to find the 
# sums and multipliers
#
# 0(n) time, #o(d) space
# n = the amount of elements in the array (not integers)
# d is the space required for the recursive call stack

def productSum(array, multiplier = 1):
	sum = 0
	for element in array:
		if type(element) is list:
			sum += productSum(element, multiplier +1)
		else:
			sum += element
	return sum * multiplier
    