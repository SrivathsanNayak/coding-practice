# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        #dummy node to make it a non-empty linked list
        dummy = tail = ListNode()
        
        #while both lists are non-empty
        while list1 and list2:
            
            #if list1 node has lower value than list2 node
            if list1.val < list2.val:
                #start with list1 node
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            #update current pointer
            tail = tail.next
        
        
        #if one of the lists is longer than the other
        #then, the shorter list will become empty after while loop
        #so we need to add remaining part of longer list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        #return the linked list after the dummy (first) node
        return dummy.next
            
        