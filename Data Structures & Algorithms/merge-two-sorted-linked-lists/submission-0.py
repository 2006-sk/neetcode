# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        #so basically I compare the values and then assign to new linkedlist
        curr1 = list1
        curr2 = list2
        new = ListNode()
        new_head = new

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                new_head.next = curr1
                new_head = new_head.next
                curr1 = curr1.next
            else:
                
                new_head.next = curr2
                new_head = new_head.next
                curr2 = curr2.next
        if curr1 is None:
            while curr2:
                new_head.next = curr2
                new_head = new_head.next
                curr2 = curr2.next  
        else:
                new_head.next = curr1
                new_head = new_head.next
                curr1 = curr1.next
        return new.next

