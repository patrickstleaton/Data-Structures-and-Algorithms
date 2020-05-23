#All traversals are O(N) time, O(N) space

#Appending nodes in order
def inOrderTraverse(tree, array):
    if tree is not None:
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
	return array

	
def preOrderTraverse(tree, array):
	#Current node, then left branch, then right.
    if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	return array


def postOrderTraverse(tree, array):
	#Left branch, then right branch, then parent
    if tree is not None:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array
