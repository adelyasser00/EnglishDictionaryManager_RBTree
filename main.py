from EngDict import EngDict

file = open("EN-US-Dictionary.txt", "r")
dictionary = EngDict()
dictionary.LoadDictionary("EN-US-Dictionary.txt")
# dictionary.InsertWord("hayam")
dictionary.RBtree.inOrderTraversal(dictionary.RBtree.root)
print("Size of dictionary= " + str(dictionary.RBtree.size))
print("Height of dictionary's tree= " + str(dictionary.RBtree.height(dictionary.RBtree.root)))
