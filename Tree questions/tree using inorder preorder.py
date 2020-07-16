class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructTree(self, inorder, preorder):

        if preorder and inorder:
            root = TreeNode(preorder.pop(0))

            left_array = inorder[0: inorder.index(root.val)]
            right_array = inorder[inorder.index(root.val) +1:]
            root.left = self.constructTree(left_array, preorder)
            root.right = self.constructTree(right_array, preorder)
            return root
        else:
            return None






preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = Solution().constructTree(inorder, preorder)
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













