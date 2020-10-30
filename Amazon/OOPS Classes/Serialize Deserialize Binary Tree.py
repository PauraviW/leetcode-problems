from collections import deque


class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

class SerializeDeserialize:
    def __init__(self):
        self.ans = []
    def serialize(self, root):
        queue = deque([root])

        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()

                self.ans.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)



    def deserialize(self, data):
        pass

obj = SerializeDeserialize()
