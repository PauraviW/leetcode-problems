from collections import deque


class TreeNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
class Serialize:
    def serialize(self, root):

        queue = deque([root])
        ansString = ''
        while queue:
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                if curr != None:
                    ansString += curr.val+','
                else:
                    ansString += 'None' + ','
                    queue.append(curr.left)
                    queue.append(curr.right)
        return ansString[:-1]
    def deserialize(self, data):
        if not data:
            return
        data = deque(data.split(','))
        root = TreeNode(data[0])
        queue = deque([root])

        while queue:
            curr = queue.popleft()
            left = data.popleft()
            right = data.popleft()
            if left:
                curr.left = TreeNode(left)
                queue.append((curr.left))
            if right:
                curr.right = TreeNode(right)
                queue.append((curr.right))
        return root
                


