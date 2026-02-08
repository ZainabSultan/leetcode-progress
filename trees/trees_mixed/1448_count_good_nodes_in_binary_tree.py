# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def preorder(node, maxsofar):
            if not node:
                return
            if node.val >= maxsofar:
                self.ans += 1
                maxsofar = node.val
            preorder(node.left, maxsofar)
            preorder(node.right, maxsofar)
        preorder(root, root.val)
        return self.ans 

        
