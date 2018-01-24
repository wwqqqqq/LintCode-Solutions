"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        result = []
        nodes = [root]
        elem = []
        while len(nodes) > 0:
            new_nodes = []
            for node in nodes:
                if node == None:
                    break
                elem.append(node.val)
                if node.left != None:
                    new_nodes.append(node.left)
                if node.right != None:
                    new_nodes.append(node.right)
            if len(elem) == 0:
                break
            nodes = new_nodes
            result.append(elem)
            elem = []
        return result   