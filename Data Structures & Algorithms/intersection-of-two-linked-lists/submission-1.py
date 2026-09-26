# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m = 0
        n = 0
        curr = headA
        while curr:
            m += 1
            curr = curr.next

        curr = headB
        while curr:
            n += 1
            curr = curr.next
        
        i = 0
        curr = None
        other = None
        if m > n:
            curr = headA
            while i < abs(m - n):
                curr = curr.next
                i += 1
            other = headB
        else:
            curr = headB
            while i < abs(m - n):
                curr = curr.next
                i += 1
            other = headA
        
        while curr and other:
            if curr == other:
                return curr
            
            curr = curr.next
            other = other.next

        return None

        