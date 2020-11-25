class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1


class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def getTop(self):
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        node.prev = None
        node.next = None
        self.size -= 1
        return node


class FreqStack:

    def __init__(self):
        self.nodeDict = defaultdict(int)
        self.freqDict = defaultdict(DLL)
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val not in self.nodeDict:
            node = Node(val)
            self.nodeDict[val] = 1
            self.freqDict[1].insert(node)
            if self.max_freq == 0:
                self.max_freq = 1
        else:
            freq = self.nodeDict[val]
            node = Node(val)
            node.freq += 1

            if node.freq > self.max_freq:
                self.max_freq = node.freq
            self.freqDict[node.freq].insert(node)

    def pop(self) -> int:
        if not self.freqDict[self.max_freq].size:
            return -1
        node = self.freqDict[self.max_freq].getTop()
        if not self.freqDict[self.max_freq].size:
            self.max_freq -= 1

        node.freq -= 1
        if not node.freq:
            del self.nodeDict[node.val]
        return node.val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()