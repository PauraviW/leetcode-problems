from collections import defaultdict


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        d = defaultdict(list)
        while head:
            if head.val in d.keys():
                if head in d[head.val]:
                    return True
            else:
                d[head.val].append(head)
            head = head.next
        return False





val = [3, 2, 0, -4]
pos = 0
val = [7]
val = [-1,-7,7,-4,19,6,-9,-5,-2,-5]
pos = 9
# i = 0
tmp = None
if len(val) > 0:

    head = ListNode(val[0])
    prev_node = head
    for i in range(1, len(val)):


        node = ListNode(val[i])
        if i == pos:
            tmp = node
        if i == len(val) - 1:
            node.next = tmp
            prev_node.next = node
            break

        prev_node.next = node
        prev_node = node
    sol = Solution().hasCycle(head)
    print(sol)
