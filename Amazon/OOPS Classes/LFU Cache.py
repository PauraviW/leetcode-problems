from collections import defaultdict


class Node:
    def __init__(self, key=None, val=None, freq=1):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None
class DLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node() # dummy
        self.tail = Node
        self.head.next = self.tail
        self.tail.prev = self.head
    def append(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def pop(self, node=None):
        if not node:
            node = node.tail.prev
        node.next.prev = node.prev
        node.prev.next = node.next
        return node

class LFUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.nodeDict = defaultdict(Node)
        self.freqDict = defaultdict(DLinkedList)
        self.size = 0
        self.min_freq = 0

    def _update(self, node):

        node = self.freqDict[node.freq].pop(node)
        if self.min_freq == node.freq and not self.freqDict[self.min_freq]:
            self.min_freq += 1
        node.freq += 1
        self.freqDict[node.freq].append(node)



    def get(self, key):
        if key not in self.nodeDict:
            return -1
        else:
            node = self.nodeDict[key]
            self.update(node)
            return node.val


    def put(self, key, value):
        if key in self.nodeDict:
            node = self.nodeDict[key]
            node.val = value
            self.update(node)
        else:
            if self.size == self.capacity:
                node = self.freqDict[self.min_freq].pop()
                del self.nodeDict[node.key]
                self.size -= 1
            node = Node(key, value)
            self.freqDict[1].append(node)
            self.min_freq = 1
            self.size += 1


