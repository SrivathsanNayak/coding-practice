# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        def dfsSum(node, curSum):
            
            if not node:
                return False
            
            curSum += node.val
            
            if not node.left and not node.right:
                return curSum == targetSum
            
            return (dfsSum(node.left, curSum) or dfsSum(node.right, curSum))
        
        return dfsSum(root, 0)