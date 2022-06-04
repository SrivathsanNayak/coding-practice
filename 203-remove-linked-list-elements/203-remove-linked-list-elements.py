# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #head node is first node of linked list
        #dummy node and previous node point to head node
        #current node is head node
        dummy = prev = ListNode(next = head)
        curr = head
        
        #while current node is not null
        while curr:
            #for next node after current node
            next = curr.next
            
            if curr.val == val:
                #remove current node
                #previous node points to the node after current node
                prev.next = next
            else:
                #we move previous to current node
                prev = curr
            
            #increment current node
            curr = next
        
        #return new head
        #pointed to by dummy node
        return dummy.next
                