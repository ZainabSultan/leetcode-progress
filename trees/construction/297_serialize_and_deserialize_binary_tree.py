# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def buildTree(self, root, res):
        if root is None:
            res.append('#')
            return res
        res.append(str(root.val))
        self.buildTree(root.left, res)
        self.buildTree(root.right, res)
        return res


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # preorder with null holder
        res = []
        return ','.join(self.buildTree(root, res))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(","))

        def ds():
            val = next(values)
            if val == "#":
                return None
                
            node = TreeNode(int(val))
            node.left = ds()
            node.right = ds()
            return node
        return ds()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
