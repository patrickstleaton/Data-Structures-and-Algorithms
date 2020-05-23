def numberOfWaysToMakeChange(n, denoms):
    #initialize array of 0s to fill the ways to make change with
	ways = [0 for amount in range(n+1)]
	#the first element will be 1, this is our base case.
	ways[0] = 1
	#Iterate through every possible denominations.
	for denom in denoms:
		#Iterate through every amount for every denomination.
		for amount in range(1, n+1):
			if denom <= amount:
				ways[amount] += ways[amount-denom]
	return ways[n]