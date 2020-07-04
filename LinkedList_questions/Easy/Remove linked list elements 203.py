class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head:
            if head.next:
                orig_node = head
                while head:
                    nextnode = head.next
                    if nextnode.val == val:
                        head.next = nextnode.next
                    head = nextnode.next
                return orig_node
            else:
                if head.val == val:
                    return head.next
                else:
                    return head


        # if head:
        #     if head.val == val:
        #         head = head.next
        #     orig_head = head
        #     if head:
        #         while head:
        #             nextnode = head.next
        #             if nextnode.val == val:
        #                 head.next = nextnode.next
        #             head = head.next
        #         return orig_head
        # else:
        #     return head
        #

val = [1, 2, 2, 1]
val = [1, 0, 1]
val = [-129, -129]
val = []
val = [1]
val = [1, 2, 6 ,3 ,4, 5 ,6]
num = 1
val = [1,1]
# val = [1,2]
# val =  [-129, -129]
# val = [1,2,3,4,5]
if len(val) > 0:
    head = ListNode(val[0])
    prev_node = head
    for i in range(1, len(val)):
        node = ListNode(val[i])
        prev_node.next = node
        prev_node = node
    sol = Solution().removeElements(head, num)
print(sol)