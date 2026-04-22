# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Logic is to define a slow and a fast pointer if they meet. then return true otherwise return false
        #Slow pointer moves two pointers at.a time and fast pointer moves one pointer at a time
        slow = head
        fast = head
        
        while slow and fast:
            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next.next

            if fast == slow:
                return True

        return False
