# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if not head:
            return head
        #I need to reverse the list first
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        cur = prev

    #List has been reversed
        carry = 0#Now we just write a while loop in which we check value if there is a carry then we move on
        value = cur.val + 1
        if value == 10:
            carry = 1
        else:
            cur.val = value
#This code works great creates new nodes if needed and adds 1
        while carry>0:
            cur.val = 0
            if cur.next:
                cur = cur.next
                value = cur.val + carry
                if value == 10:
                    cur.val = 0
                    carry = 1
                else:
                    cur.val = value
                    carry = 0
            else:
                temp = ListNode()
                cur.next = temp
                cur = cur.next
                cur.val = carry
                carry = 0
        
        new_prev = None
        currr = prev
        while currr:
            temp = currr.next
            currr.next = new_prev
            new_prev = currr
            currr = temp
        cur = new_prev
        
        return new_prev
            





        
