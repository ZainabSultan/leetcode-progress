# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float('-inf')
        def postorder(node):
            if not node:
                return 0
            
            left_gain = max(0, postorder(node.left))
            right_gain = max(0, postorder(node.right))

            current_gain = node.val + left_gain + right_gain
            self.global_max = max(self.global_max, current_gain)
            return node.val + max(left_gain, right_gain) # path to return upward is only from one side
        postorder(root)
        return self.global_max

        