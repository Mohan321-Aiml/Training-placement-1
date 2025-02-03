# Definition for a binary tree node.
# class TreeNode(object):
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left, right):
            if left > right:
                return None  # Base case: no elements in this range

            # Middle index to balance the BST
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            # Recursively construct left and right subtrees
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        # Call the helper function with full array bounds
        return helper(0, len(nums) - 1)
        
