# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def check_balance(node):
            if not node:
                return 0  # Высота пустого дерева равна 0

            left_height = check_balance(node.left)
            if left_height == -1:
                return -1  # Левое поддерево несбалансировано

            right_height = check_balance(node.right)
            if right_height == -1:
                return -1  # Правое поддерево несбалансировано

            if abs(left_height - right_height) > 1:
                return -1  # Несбалансированное дерево

            return max(left_height, right_height) + 1

        return check_balance(root) != -1
