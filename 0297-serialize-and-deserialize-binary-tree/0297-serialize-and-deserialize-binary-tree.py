# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""

        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            currentNode = queue.popleft()
            if currentNode:
                res.append(str(currentNode.val))
                queue.append(currentNode.left)
                queue.append(currentNode.right)
            else:
                res.append("None")
        
        return ",".join(res)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
    
        if not data: return None

        elements = data.split(",")
        root = TreeNode(int(elements[0]))
        
        queue = deque([root])

        idx = 1
        while queue:
            currentNode = queue.popleft()
            if elements[idx] != "None":
                currentNode.left = TreeNode(int(elements[idx]))
                queue.append(currentNode.left)
            idx += 1

            if elements[idx] != "None":
                currentNode.right = TreeNode(int(elements[idx]))
                queue.append(currentNode.right)            
            idx += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))