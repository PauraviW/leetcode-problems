class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev_head = ListNode()
        orig_head = l1
        while l1 and l2:

            if l2.val == l1.val:
                tmp1 = l1.next
                l1.next = l2
                tmp2 = l2.next
                l2.next = tmp1
                l2 = tmp2
                l1 = l1.next
            elif l1.val < l2.val:
                prev_head = l1.next
                tmp = l2.next
                l1.next = l2
                l2.next = prev_head
                l1 = l1.next
                l2 = tmp

            else:
                if prev_head.next == None:
                    orig_head = l2
                prev_head.next = l2
                tmp = l2.next
                l2.next = l1
                prev_head = l2
                l2 = tmp

        return orig_head








val1 = [1, 2, 4]
val2 = [1, 2, 3]
val1 = [1, 3]
val2 = [2, 4]
if len(val1) > 0 and len(val2) > 0:
    head1 = ListNode(val1[0])
    prev_node = head1
    for i in range(1, len(val1)):
        node = ListNode(val1[i])
        prev_node.next = node
        prev_node = node
    head2 = ListNode(val2[0])
    prev_node = head2
    for i in range(1, len(val2)):
        node = ListNode(val2[i])
        prev_node.next = node
        prev_node = node
    sol = Solution().mergeTwoLists(head1, head2)
    while sol:
        print(sol.val)
        sol = sol.next

