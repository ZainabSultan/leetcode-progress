### serialisation vs deserialisation

my first attempt was doing preorder, inorder - which fails in case of duplicates. 

class Codec:
    def preorder(self,root, res):
        if root is None:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)
    
    def inorder(self, root, res):
        if root is None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        pre = []
        self.preorder(root, pre)
        ino = []
        self.inorder(root, ino)
        return(str(pre) +'R'+ str(ino))


    def buildTree(self, pre, ino):
        if pre == [] or ino == []:
            return None
        root = TreeNode(pre[0])
        mid = ino.index(pre[0]) 
        root.left = self.buildTree(pre[1:mid+1], ino[:mid])
        root.right = self.buildTree(pre[mid+1:], ino[mid+1:])
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        pre = eval(data.split('R')[0])
        ino = eval(data.split('R')[1])
        tree=self.buildTree(pre, ino)
        return tree

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
