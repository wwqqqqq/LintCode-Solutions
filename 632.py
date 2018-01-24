"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        if root.left == None and root.right == None:
            return root.val
        elif root.left == None:
            right = self.maxNode(root.right)
            if right>root.val:
                return right
            else:
                return root.val
        elif root.right == None:
            left = self.maxNode(root.left)
            if left>root.val:
                return left
            else:
                return root.val
        else:
            left = self.maxNode(root.left)
            right = self.maxNode(root.right)
            if left>right:
                m = left
            else:
                m = right
            if root.val>m:
                m = root.val
            return m

#{1,-5,3,1,2,-4,-5}
a = Solution(1)
x = Solution(-5)
y = Solution(4)
a.left = x
a.right = y
root = a
b = Solution(1)
c = Solution(2)
x.left = b
x.right = c
b = Solution(-4)
c = Solution(-5)
y.left = b
y.right = c
print(root.maxNode(a))
