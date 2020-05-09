#O(log(N)) time, O(1) space
#Traverse the tree and calculate absolute value to find the closest value to target.
def findClosestValueInBst(tree, target):
    return findClosestHelper(tree, target, float('inf'))

def findClosestHelper(tree, target, closest):
	currentNode = tree
	while currentNode is not None:
		if abs(target-closest) > abs(target-currentNode.value):
			closest = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
	return closest