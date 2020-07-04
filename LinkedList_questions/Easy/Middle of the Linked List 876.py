class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        orig_head = head
        L = 0
        while head:
            L += 1
            head = head.next
        i = 0
        while i < L//2:
            orig_head = orig_head.next
            i += 1
        return orig_head









val = [1,2,3,4,5,6]
# val = [1,2,3,4,5]
head = ListNode(val[0])
prev_node = head
for i in range(1, len(val)):
    node = ListNode(val[i])
    prev_node.next = node
    prev_node = node
sol = Solution().middleNode(head)
print(sol.val)