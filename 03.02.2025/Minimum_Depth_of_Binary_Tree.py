# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):

        def check_balance(node, d, a):
            if not node and a:
                return d-1
            elif not node:
                return 10**5+1


            left = check_balance(node.left, d+1, not node.left and not node.right)
            right = check_balance(node.right, d+1, not node.left and not node.right)

            return min(left, right)

        return check_balance(root, 1, True)
