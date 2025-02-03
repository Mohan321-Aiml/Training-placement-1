# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if q is None and p is None:
            return True
        if q is None or p is None:
            return False
        if(p.val==q.val):
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False
        
