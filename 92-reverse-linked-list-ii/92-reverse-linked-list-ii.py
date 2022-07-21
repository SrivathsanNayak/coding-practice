# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        cur, prev = head, None
        
        #to reach required starting position
        while left > 1:
            prev, cur = cur, cur.next
            left, right = left - 1, right - 1
            
        tail, con = cur, prev
        
        while right:
            #traversal while reversing nodes
            cur.next, prev, cur = prev, cur, cur.next
            right -= 1
            
        if con:
            con.next = prev
        else:
            head = prev
            
        tail.next = cur
        return head