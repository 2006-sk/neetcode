# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #compare at head of all of the linked lists then cut the list and make new head, do this until all linked lists empty
        
        length = len(lists)
        #Approach 1
        #Imagine it is an array and I have to sort arrays inside the array to make the 
        # Single sorted array.
        #How do I do that
        #So i traverse the list until, I compare the head nodes of each of the array
        #and store the idnex of that array in the big array
        #then I go there and remove tthe head of that array 
        #After doing that the loop ccontinues until something.
        #so first I define a while loop that loops through each linekdlist and finds the total tnumber of numbers.
        if lists == None:
            return None
        
        count = 0
        for i in range(length):
            curr = lists[i]
            while curr != None:
                count += 1
                curr = curr.next
        if count == 0:
            return None
        new_list = ListNode(0)
        head = new_list
        while count > 0:
            #What all do I have to do here:
            #First of all I need to traverse and find the node with the smallest number
            index = -1
            minimum = float('inf')
            for i in range(length):
                if lists[i] == None:
                    continue
            #We use val to access the head of the 
                if lists[i].val < minimum:
                    minimum = lists[i].val
                    index = i
                
            #We have the minimum and the minimum index.
            #Now we remove the value from head
            
            node = lists[index]
            # Move the pointer in the array forward
            if lists[index].next == None:
                lists[index] = None
            else: lists[index] = lists[index].next

            #We have moved forward and stored node 
            head.next = node
            head = head.next
            count -=1

        return new_list.next



                

            











