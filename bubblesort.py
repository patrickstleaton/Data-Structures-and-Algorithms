def bubbleSort(array):
	#Iterate through the array starting at the second index.
    for i in range(1, len(array)):
	    #Compare each index location with the previous loop's.
		for j in range(0, len(array)):
			#If the previous location is less than the next, swap.
			if array[i] < array[j]:
				array[i], array[j] = array[j], array[i]
	return array