# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #set up an algo to find the nth node from end so if there are total 8 elements , find 2 then 8-2 is 6+1 = 7 that'show we find int
        #if length is 2 and have to find second one then 2-2+1 = 1
        #if there are 4 then 4-2+1 so 3rd elemnt from start
        if head.next is None:
            return None
        count = 1
        cur = head
        while cur:
            cur = cur.next
            count+= 1

        curr = head
        midpoint = count - n -1

        if midpoint <= 0:
            temp = curr.next
            curr.next = None
            curr = temp
            return temp

        while midpoint > 0:

            midpoint -= 1
            temp = curr
            curr = curr.next
        temp2 = curr.next
        temp.next = temp2
        curr.next = None
        return head
            
            

