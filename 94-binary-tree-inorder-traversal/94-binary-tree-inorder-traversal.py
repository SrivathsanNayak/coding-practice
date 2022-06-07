# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        #inorder - left-subtree -> root -> right-subtree
        
        l = []
        
        if root.left:
            for i in self.inorderTraversal(root.left):
                l.append(i)
        
        l.append(root.val)
        
        if root.right:
            for i in self.inorderTraversal(root.right):
                l.append(i)
                
        return l