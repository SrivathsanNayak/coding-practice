# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #Floyd tortoise and hare algo
        #initialize both pointers from head
        slow = head
        fast = head
        
        #if fast.next is null, then that means it has reached end of list
        #so no cycle if fast.next is null
        while fast and fast.next:
            #move slow pointer by one
            slow = slow.next
            
            #move fast pointer by two
            fast = fast.next.next
            
            #if fast meets slow pointer
            #that means it has entered a cycle
            if slow == fast:
                return True
            
        return False
        