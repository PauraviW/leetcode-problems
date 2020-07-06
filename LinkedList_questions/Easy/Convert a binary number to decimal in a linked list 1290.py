
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        binary = ''
        while head:
            binary += str(head.val)
            print(head.val)
            head = head.next

        return int(binary, 2)

# head = ListNode(1)
# fn = ListNode(0)
# head.next = fn
# sn = ListNode(1)
# fn.next = sn
values = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
head = ListNode(values[0])
prev_node = head
for i in range(1, len(values)):

    node = ListNode(values[i])
    prev_node.next = node
    prev_node = prev_node.next
sol = Solution().getDecimalValue(head)
print(sol)