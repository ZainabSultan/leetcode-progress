# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.hash = {}
        def inorder(node):
            if not node:
                return False
            l = inorder(node.left)
            diff = k - node.val

            if node.val in self.hash:
                return True
            else:
                self.hash[diff] = node.val
            r = inorder(node.right)
            
            return l or r
        return inorder(root)

        
