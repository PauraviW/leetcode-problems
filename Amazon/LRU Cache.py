# LRU cache
# get -1, put - remove the least recently used item
from collections import defaultdict

class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def update(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    def pop(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev



class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashMap = defaultdict(Node)
        self.cache = DLinkedList()
        self.size = 0
    def get(self, key):
        if key not in self.hashMap:
            return -1
        else:
            node = self.hashMap[key]
            self.cache.update(node)
            return node

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.hashMap:
            node = self.hashMap[key]
            node.val = value
            self.cache.update(node)
        else:
            if self.size == self.capacity:
                self.size -= 1
                self.cache.pop()
                del self.hashMap[key]
            newNode = Node(key, value)
            self.cache.addNode(newNode)
            self.hashMap[key] = newNode
            self.size += 1

