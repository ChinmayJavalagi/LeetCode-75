# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def delete(root, key):
            if root is None:
                return None
            if key>root.val:
                root.right = delete(root.right, key)
            elif key<root.val:
                root.left = delete(root.left, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                else:
                    inosucc = self.inorderSuccessor(root.right)
                    root.val = inosucc
                    root.right = delete(root.right, inosucc)
            return root
        return delete(root, key)

    def inorderSuccessor(self, root):
        while root.left:
            root = root.left
        return root.val
