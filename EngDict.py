import astropy

from RBTree import *


class EngDict:

    def __init__(self):
        self.RBtree = RBTree()

    def LoadDictionary(self, filename):
        file = open(filename, "r")
        while True:
            line = str.strip(file.readline())
            if not line:
                break
            self.RBtree.insert(line)

    def PrintDictionarySize(self):
        print(f"dictionary contains {self.RBtree.size} words")

    def LookUpWord(self, word):
        x = self.RBtree.root
        while x != self.RBtree.nil:
            # move down the RBtree until we reach the target leaf node
            temp = x.value
            if str.lower(temp) > str.lower(word):
                x = x.left
            elif str.lower(temp) < str.lower(word):
                x = x.right
            else:
                print("Word is found in the dictionary!")
                return True
        print("Word is not found in the dictionary!")
        return False

    def InsertWord(self, word):
        flag = self.LookUpWord(word)
        if not flag:
            self.RBtree.insert(word)
            print(f"{word} has successfully been inserted to the dictionary!")
        else:
            print("ERROR:word already exists!\nInsert operation canceled!")
