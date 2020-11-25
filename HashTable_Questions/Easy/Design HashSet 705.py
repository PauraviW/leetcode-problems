class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet = set()

    def add(self, key: int) -> None:
        self.hashSet.add(key)

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hashSet:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

class MyHashSet2(set):

    def viewContents(self):
        return list(super())
    def add(self, key: int) -> None:
        self.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            super().remove(key)
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        print(self)
        return key in self

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet2()
obj.add(1)
obj.remove(2)
param_3 = obj.contains(3)
print(param_3)
# print(obj.viewContents())