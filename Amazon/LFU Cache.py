from collections import defaultdict


class Node:
    def __init__(self, val= None):
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1
class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.head
        self.head.next = self.tail
    def pop(self, node=None):
        if node:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
        else:
            node = self.tail.prev
            node.prev.next = self.tail
            self.tail.prev = node.prev

        return node
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

class LFUCache:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.freqDict = defaultdict(DLL)
        self.nodeDict = defaultdict(Node)
        self.min_freq = 1
    def update(self, node):
        freq = node.freq
        self.freqDict[freq].pop(node)
        if freq == self.min_freq and not self.freqDict[self.min_freq]:
            self.min_freq += 1
        node.freq += 1
        self.freqDict[node.freq].insert(node)
        # return node

    def get(self, key):
        if key not in self.nodeDict:
            return -1
        else:
            node = self.nodeDict[key]
            self.update(node)
            return node.val
    def put(self, key, value):
        if key in self.nodeDict:
            node = self.freqDict[key]
            node.val = value
            self.update(node)
        else:
            if self.size == self.capacity:
                node = self.freqDict[self.min_freq].pop()
                del self.nodeDict[node.key]
                self.size -= 1
            node = Node(key, value)
            self.nodeDict[key] = value
            self.min_freq = 1
            self.freqDict[self.min_freq].insert(node)
            self.size += 1






