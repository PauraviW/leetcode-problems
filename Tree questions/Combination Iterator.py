class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.char = characters
        self.cl = combinationLength
        self.root = TreeNode("")
        self.traverse(self.root, 0)
        self.display(self.root)

    def traverse(self, root, index):
        l = []
        for i in range(index + 1, len(self.char) - self.cl + 1):
            node = TreeNode(self.char[i])
            l.append(node)
            self.traverse(node, i)
        root.children = l
    def display(self, root):
        if root:
            print(root.val)
            for child in root.children:
                self.display(child)
            print("---------------------")


    # def next(self) -> str:

    # def hasNext(self) -> bool:

# Your CombinationIterator object will be instantiated and called as such:
characters = 'abcde'
combinationLength = 3
obj = CombinationIterator(characters, combinationLength)


# param_1 = obj.next()
# param_2 = obj.hasNext()