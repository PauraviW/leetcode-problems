class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructTree(self, inorder, postorder):
        if inorder and postorder:

            root = TreeNode(postorder.pop())
            left_array = inorder[0:inorder.index(root.val)]
            right_array = inorder[inorder.index(root.val) + 1:]
            root.right = self.constructTree(right_array, postorder)
            root.left = self.constructTree(left_array, postorder)
            return root
        else:
            return None





postorder = [9,15,7,20,3]
inorder = [9,3,15,20,7]
root = Solution().constructTree(inorder, postorder)
vals = []
stack = [root]
while stack:
    node = stack.pop(0)
    vals.append(node.val)
    if node.left:
        stack.append(node.left)
    if node.right:
        stack.append(node.right)

print(vals)










