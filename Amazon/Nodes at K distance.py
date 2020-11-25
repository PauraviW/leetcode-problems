
class Solution:
    def Kdistance(self, root, target, k =0):

        self.hashmap = defaultdict(Node)
        self.traverse(root, None)
        queue = deque(target)
        j = 0
        ans = []
        while queue and j < k:
            n = len(queue)
            for i in range(n):

                curr = queue.popleft()
                if j == k :
                    ans.append(curr.val)
                    continue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                queue.append[self.hashmap[curr]]
            j += 1
        return ans


    def traverse(self, root, parent):
        if root:
            self.hashmap[root] = parent
            if root.left:
                self.traverse(root.left, root)

            if root.right:
                self.traverse(root.right, root)

