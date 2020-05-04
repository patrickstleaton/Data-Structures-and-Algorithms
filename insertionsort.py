def insertionSort(array):
	#Iterate through the array, assuming the first index is sorted initially.
	for i in range(1, len(array)):
		j=i
		#For each index i, step backwards to see if everything is sorted in the sublist until you reach the beginning. 
		while j > 0 and array[j] < array[j-1]:
			array[j-1], array[j] = array[j], array[j-1]
			j-=1
	return array