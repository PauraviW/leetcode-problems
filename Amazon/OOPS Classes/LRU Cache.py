from collections import defaultdict
class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self, capacity):
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0
    def addNode(self, key, value):
        node = Node(key, value)
        delKey = None
        if self.len >= self.capacity:
            delKey = self.popTail()
            self.len -= 1
        self.performUpdates(node)
        self.len += 1
        return node, delKey
    def popTail(self):
        res = self.tail.prev
        res.prev.next = self.tail
        self.tail.prev = res.prev
        return res.key

    def updateNode(self, node, value):
        node.value = value
        nprev = node.prev
        nnext = node.next
        nprev.next = nnext
        nnext.prev = nprev
        self.performUpdates(node)


    def get(self, node):
        nprev = node.prev
        nnext = node.next
        nprev.next = nnext
        nnext.prev = nprev
        self.performUpdates(node)
        return node.key
    def performUpdates(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node






class LRUCache:
    def __init__(self, capacity):

        self.hashtable = defaultdict(Node)
        self.dlist = DoubleLinkedList(capacity)

    def put(self, key, value):
        if key in self.hashtable:
            self.dlist.updateNode(self.hashtable[key], value)
        else:
            node, delKey = self.dlist.addNode(key, value)
            if delKey:
                del self.hashtable[delKey]
            self.hashtable[key] = node
    def get(self, key):
        if key in self.hashtable:
            return self.dlist.get(self.hashtable[key])
        else:
            return -1



lRUCache = LRUCache(1);
# print(lRUCache.put(1, 1)); # cache is {1=1}
# print(lRUCache.put(2, 2)); # cache is {1=1, 2=2}
# print(lRUCache.get(1));    # return 1
# print(lRUCache.put(3, 3)); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache.get(2));    # returns -1 (not found)
# print(lRUCache.put(4, 4)); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache.get(1));    # return -1 (not found)
# print(lRUCache.get(3));    # return 3
# print(lRUCache.get(4));

print(lRUCache.put(2, 1));
print(lRUCache.get(2));
# ["LRUCache","put","get"]
# [[1],[2,1],[2]]