# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        while curr:
            if stack[-1].val != curr.val:
                return False
            
            stack.pop()
            curr = curr.next
        
        return True

        