# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d = 0
        
        def dfs(root):
            if not root:
                return 0
            
            left, right = dfs(root.left), dfs(root.right)
            
            self.d = max(self.d, left + right)
            return max(left, right) + 1
        
        dfs(root)
        return self.d