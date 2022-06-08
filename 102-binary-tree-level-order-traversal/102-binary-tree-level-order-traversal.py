# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        l = []
        
        #use queue, for implementing bfs
        q = collections.deque()
        q.append(root)
        
        #go through all nodes
        while q:
            level = []
            for i in range(len(q)):
                #pop element from front of queue
                node = q.popleft()
                if node:
                    level.append(node.val)
                    #if node has child nodes
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                l.append(level)
                
        return l
        