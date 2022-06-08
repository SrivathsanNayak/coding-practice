# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        levels = 0
        
        if not root:
            return 0
        
        q = collections.deque()
        q.append(root)
        
        while q:
            l = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    l.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if l:
                levels += 1
        
        return levels
            
        