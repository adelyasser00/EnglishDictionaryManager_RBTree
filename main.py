from EngDict import EngDict

file = open("EN-US-Dictionary.txt", "r")
dictionary = EngDict()
dictionary.LoadDictionary("EN-US-Dictionary.txt")
#dictionary.InsertWord("hayam")

dictionary.LoadDictionary("EN-US-Dictionary.txt")

dictionary.RBtree.inOrderTraversal(dictionary.RBtree.root)