class Node:
    def __init__(self, val):
        self.val = None
        self.min = None
class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val):

        node = Node(val)
        if not self.stack:
            node.min = val

        else:
            currmin = self.stack[-1].min
            if val < currmin:
                currmin = val
            node.min = currmin
        self.stack.append(node)
    def pop(self):
        self.stack.pop()
    def getMin(self):
        if self.stack:
            return self.stack[-1].min
        else:
            return -1
