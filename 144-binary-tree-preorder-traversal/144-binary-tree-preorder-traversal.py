# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root
        
        #preorder - root -> left-subtree -> right-subtree
        
        l = [root.val]
        
        if root.left:
            for i in self.preorderTraversal(root.left):
                l.append(i)
                
        if root.right:
            for i in self.preorderTraversal(root.right):
                l.append(i)
            
        return l