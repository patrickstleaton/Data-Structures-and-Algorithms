def isValidSubsequence(array, sequence):
    #Set two pointers, one of each list.
	array_index = 0
	sequence_index = 0
	#While we are still in bounds of our lists...
	while array_index < len(array) and sequence_index < len(sequence):
		#If the pointer for our array matches the pointer for our sequence...
		if array[array_index] == sequence[sequence_index]:
			#Set our sequence pointer to the next element for checking
			sequence_index +=1
		#Set our array pointer to the next element to be checked 
		#within the next iteration
		array_index +=1
	#Return whether or not the sequence pointer reached the end of the list.
	return sequence_index == len(sequence)