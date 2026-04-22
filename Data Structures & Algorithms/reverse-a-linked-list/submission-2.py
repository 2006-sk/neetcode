# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        arr = []
        currnode = head
        while currnode:
            arr.append(currnode.val)
            currnode = currnode.next
        currnode = head
        while currnode:
            currnode.val = arr.pop() # pop() takes the last element (reverse order)
            currnode = currnode.next
        return head
