from RBTree import *


class EngDict:

    def __init__(self):
        self.RBtree = RBTree()

    def LoadDictionary(self, filename):
        file = open ( filename, "r" )
        line = file.readline ()
        while line:
            line = file.readline ()
            self.RBtree.insert ( line )

    def PrintDictionarySize(self):
        print ( f"dictionary contains {self.RBtree.size} word" )

    def LookUpWord(self, word):
        x = self.RBtree.root

        while x != self.RBtree.nil or x.value != word:
            # move down the RBtree until we reach the target leaf node
            if x.value > word:
                x = x.left
            elif x.value < word:
                x = x.right
            else:
                print ( "YES" )
                return True
        print ( "NO" )
        return False

    def InsertWord(self, word):
        flag = self.LookUpWord ( word )
        if (flag):
            self.RBtree.insert ( word )
        else:
            print ( "ERROR:word already exists!" )



