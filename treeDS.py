class TreeNode:
    def __init__(self,data):
        self.data = data;
        self.children = []
        self.parent = None

    def addElement(self,element):
        element.parent = self
        self.children.append(element)

    def label(self):
        count  = 0
        parent = self.parent
        while parent:
            count+=1
            parent = parent.parent
        return count



    def printTree(self):
        if self.label():
            print(" "*3*self.label()+"|__",end = "")

        print(self.data)
        for child in self.children:
            child.printTree()

# this is the simpl code

electronic = TreeNode("electronic")

computer  = TreeNode("computer")
wood = TreeNode("wood")

laptop = TreeNode("laptop")
desktop = TreeNode("desktop")
mobile  =  TreeNode("mobile")


almera = TreeNode("almera")
table = TreeNode("table")
chair = TreeNode("chair")

electronic.addElement(computer)
electronic.addElement(wood)

computer.addElement(laptop)
computer.addElement(desktop)
computer.addElement(mobile)

wood.addElement(almera)
wood.addElement(table)
wood.addElement(chair)

electronic.printTree()

# print(computer.label())
