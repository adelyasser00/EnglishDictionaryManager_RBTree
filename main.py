from EngDict import EngDict

def DictionaryFunctionality():
    print("Welcome to the English Dictionary manager!\nPlease enter the file name:")
    filename  = input()
    dictionary = EngDict ()
    dictionary.LoadDictionary ( filename )

    while True:
        print("Choose a task:\n1.Print dictionary size\n2.Insert word\n3.Look-up a word\n4.Save and Exit\n5.Print dictionary content ")
        try:
            choice = int(input())

            if choice == 1:
                dictionary.PrintDictionarySize()
                print("Tree height is", dictionary.RBtree.height(dictionary.RBtree.root))

            elif choice == 2:
                print("Enter word")
                word = input()
                dictionary.InsertWord ( str(word) )
                dictionary.PrintDictionarySize ()
                print("Tree height is", dictionary.RBtree.height(dictionary.RBtree.root))

            elif choice == 3:
                print ( "Enter word" )
                word = input ()
                dictionary.LookUpWord(word)

            elif choice == 4:
                f = open(filename, "w")
                f.close()
                f = open(filename, "a")
                dictionary.RBtree.inOrderWrite(dictionary.RBtree.root, f)
                f.close()
                break

            elif choice == 5:
                dictionary.RBtree.inOrderTraversal(dictionary.RBtree.root)

            else:
                print("Not a valid choice")

        except ValueError as e:
            print("Not a valid choice")



# Calling main program method
DictionaryFunctionality()

# Our used dictionary file name for easy access
#filename = "EN-US-Dictionary.txt"


