# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        #postorder - left-subtree -> right-subtree -> root
        
        l = []
        
        if root.left:
            for i in self.postorderTraversal(root.left):
                l.append(i)
                
        if root.right:
            for i in self.postorderTraversal(root.right):
                l.append(i)
                
        l.append(root.val)
        
        return l
        