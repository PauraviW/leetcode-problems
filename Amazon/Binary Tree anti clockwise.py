data = [1,2,3,4,5,6]
class Tree:
    def __init__(self):
        self.leftb = []
        self.rightb = []
        self.leaves  = []

    def printTree(self, root):
        ans = [root.val]

        self.printLeft(root.left)
        self.printRight(root.right)
        self.printLeaves(root)
        print(self.leftb, self.rightb, self.leaves)

    def printLeft(self, root):
        if root:
            self.leftb.append(root.val)
            if root.left:
                self.printLeft(root.left)
            elif root.right:
                self.printLeft(root.right)

    def printRight(self, root):
        if root:
            self.rightb.append(root.val)
            if root.right:
                self.printRight(root.right)
            elif root.left:
                self.printRight(root.left)
    def printLeaves(self, root):
        if root:
            if not root.left and not root.right:
                self.leaves.append(root.val)
                if root.left:
                    self.printLeaves(root.left)
                if root.right:
                    self.printLeaves(root.right)
