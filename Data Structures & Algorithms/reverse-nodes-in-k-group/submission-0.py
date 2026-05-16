# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #First we will coiunt the number of nodes, and calcualte the numbe rof iterations we will be doing. 
        #So total number of nodes and then I will use the floor division // to get the numbe rof times to run the for loop

        node = head
        count = 0   
        while node != None:
            count += 1
            node = node.next

        cycles = count // k
        
        #Now we have correct cycles and correct number of nodes in the linked list
        # now what we do is we run a for loop for the cycle
        #Then we run a while loop until we reverse the first k nodes. 
        # then we attach the first node to the start of the next group's first node

        # We need to store the head's positions before starting reversing 
        dummy = ListNode(0, head)
        groupPrev = dummy
        cur = head

        for i in range(cycles):
    # 'temper' will become the tail of this reversed group
            temper = cur 
            prev = None 
    
    # Standard reversal for k nodes
            for _ in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
    
    # 1. Connect previous group's tail to current group's new head (prev)
            groupPrev.next = prev
    
    # 2. Connect current group's new tail (temper) to the next group's start (cur)
            temper.next = cur
    
    # 3. Move groupPrev forward to the tail of our recently reversed group
            groupPrev = temper

        return dummy.next






