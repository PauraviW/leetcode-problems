# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.min = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    def addNode(self, node):
        if self.head.next:
            currMin = self.head.next.val

        if currMin:
            if node.val < currMin:
                node.min = node.val
            else:
                node.min = currMin

        node.next = self.head.next
        self.head.next = node
    def pop(self):
        if self.head.next:
            node = self.head.next
            self.head.next = node.next
            return node
        else:
            return -1
class MinStack:
    def __init__(self):
        self.minVal = float('inf')
        self.minElement = None
        self.stack = LinkedList()
        self

    def push(self, val):

        node = Node(val)
        if val < self.minVal:
            self.minVal = val
            self.minElement = node

        self.stack.addNode(node)
    def pop(self):
        node = self.stack.pop()
        return node
    def top(self):
        if self.stack.head.next:
            return self.stack.head.next.val
        else:
            return -1
    def getMin(self):
        if self.stack.head.next:
            return self.stack.head.next.min
        else:
            return -1
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
print(minStack.pop())
print(minStack.top()) # return 0
print(minStack.getMin())