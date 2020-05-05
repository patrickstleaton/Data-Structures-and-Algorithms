def selectionSort(array):
	currentIdx=0
	while currentIdx < len(array)-1:
		smallestNumIdx = currentIdx
		for i in range(currentIdx + 1, len(array)):
			if array[smallestNumIdx] > array[i]:
				smallestNumIdx = i
		array[currentIdx], array[smallestNumIdx] = array[smallestNumIdx], array[currentIdx]
		currentIdx +=1
	return array	                                                                      