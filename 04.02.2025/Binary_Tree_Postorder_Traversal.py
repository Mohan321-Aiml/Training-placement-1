# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rec(self,root,path):
        if not root:
            return 
        self.rec(root.left,path)
        self.rec(root.right,path)
        
        path.append(root.val)
        

    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        path=[]
        self.rec(root,path)
        return path

   
        
