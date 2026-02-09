# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.nums = []
        def preorder(node, num):
            if not node:
                return
            num *=10
            num+=node.val
            if not node.left and not node.right:
                self.nums.append(num)
            preorder(node.left, num)
            preorder(node.right, num)
        preorder(root, 0)
        return sum(self.nums) 
            
