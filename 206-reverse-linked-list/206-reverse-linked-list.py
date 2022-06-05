# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev #first node points to None
            #other nodes will point to their previous element
            
            prev = curr #updating prev element
            curr = nextNode #updating curr element
        
        return prev    
        