class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        orig = head
        ll = []
        while head:
            ll.append(head.val)
            head = head.next
        ll = ll[::-1]
        head = ListNode(ll[0])
        prev_node = head
        for i in range(1, len(ll)):
            node = ListNode(ll[i])
            prev_node.next = node
            prev_node = prev_node.next
        return head











values = [1,2,3,4,5]
head = ListNode(values[0])
prev_node = head
for i in range(1, len(values)):
    node = ListNode(values[i])
    prev_node.next = node
    prev_node = prev_node.next
sol = Solution().reverseList(head)
while sol:
    print(sol.val)
    sol = sol.next