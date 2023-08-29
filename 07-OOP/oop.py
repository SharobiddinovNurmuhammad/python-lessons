class PrintList:

    def __init__(self, myList):
        self.myList = myList

    def __repr__(self):
        return str(self.myList)
    

printList = PrintList(['a', 'b', 'c'])

print(printList.__repr__())
print(printList)