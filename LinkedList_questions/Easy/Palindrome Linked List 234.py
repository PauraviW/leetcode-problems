# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ll = []
        if head:
            while head:
                ll.append(head.val)
                head = head.next
            mid = len(ll)//2
            if len(ll)%2 == 0:
                if ll[0:mid] == ll[mid:][::-1]:
                    return True
                else:
                    return False
            else:
                if ll[0:mid] == ll[mid+1:][::-1]:
                    return True
                else:
                    return False
        else:
            return True





val = [1, 2, 2, 1]
val = [1,0,1]
val = [-129, -129]
val = []
val = [1]
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
    sol = Solution().isPalindrome(head)
else:
    sol = Solution().isPalindrome(ListNode())
print(sol)