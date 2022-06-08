# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return False
        
        def checkMirror(l,r):
            
            if l and r and l.val == r.val:
                return checkMirror(l.left, r.right) and checkMirror(l.right, r.left)
            
            return l == r
        
        return checkMirror(root.left, root.right)