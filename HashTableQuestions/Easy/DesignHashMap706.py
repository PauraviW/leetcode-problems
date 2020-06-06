import collections
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hashTable[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.hashTable:
            return self.hashTable[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hashTable:
            del self.hashTable[key]


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,1)
param_2 = obj.get(6)
print(param_2)
obj.remove(2)
hashMap = MyHashMap()
hashMap.put(1, 1);
hashMap.put(2, 2);
print(1,hashMap.get(1));            # returns 1
print(3, hashMap.get(3));
print(2, hashMap.get(2));# returns -1 (not found)
hashMap.put(2, 1);          # update the existing value
print(2, hashMap.get(2));
hashMap.remove(2);          # remove the mapping for 2
print(2, hashMap.get(2));
hashMap.get(2);            # returns -1 (not found)
print(2, hashMap.get(2));