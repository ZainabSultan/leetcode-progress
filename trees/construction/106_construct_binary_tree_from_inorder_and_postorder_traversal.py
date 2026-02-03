# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder == [] or postorder == []:
            return None
        root_value = postorder[-1]
        root  = TreeNode(root_value)
        mid = inorder.index(root_value)
        root.left = self.buildTree( inorder[:mid], postorder[:mid])
        root.right = self.buildTree( inorder[mid+1:], postorder[mid:-1])
        return root
