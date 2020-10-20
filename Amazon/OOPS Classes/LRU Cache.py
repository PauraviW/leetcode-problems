from collections import defaultdict


class Node:
    def __init__(self,  key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class DoubleLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.len = 0
    def addNode(self, key, value):
        node = Node(key, value)
        delKey = None
        if not self.head:
            self.head = node
            self.tail = node
            self.len += 1
        elif self.len >= self.capacity:
            delKey = self.tail.key
            if self.len == 1:
                self.head = node
                self.tail = node
                # return delKey
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node.next
                self.tail = self.tail.prev
                self.tail.next = None

        elif self.len < self.capacity:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.len += 1




        return node, delKey

class LRUCache:
    def __init__(self, capacity):
        self.dlist = DoubleLinkedList(capacity)
        self.hashTable = defaultdict(Node)
    def get(self, key):
        if key in self.hashTable:
            node = self.hashTable[key]
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
            if len(self.hashTable) != 1:
                if self.dlist.tail == node:
                    self.dlist.tail = node.prev
            node.next = self.dlist.head
            self.dlist.head.prev = node
            self.dlist.head = node
            return node.val
        else:
            return -1
    def put(self, key, value):

        if key not in self.hashTable:
            node, delKey = self.dlist.addNode(key, value)
            self.hashTable[key] = node
            if delKey:
                del self.hashTable[delKey]


    # def send_to_end(self, node):

lRUCache = LRUCache(2);
print(lRUCache.put(1, 1)); # cache is {1=1}
print(lRUCache.put(2, 2)); # cache is {1=1, 2=2}
print(lRUCache.get(1));    # return 1
print(lRUCache.put(3, 3)); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    # returns -1 (not found)
# lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    # return -1 (not found)
# lRUCache.get(3);    # return 3
# lRUCache.get(4);