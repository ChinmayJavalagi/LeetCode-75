# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def helper(self,root,l):
        if root is None:
            return
        if root.left==None and root.right==None:
            l.append(root.val)
            return 
        self.helper(root.left,l)
        self.helper(root.right,l)
        return l


    def leafSimilar(self, root1, root2):
        if root1.left is None and root1.right is None:
           if root2.left is None and root2.right is None and root1.val == root2.val: 
               return True
           else:
                return False
        li,l1 = [],[]
        li = self.helper(root1,li)
        l1 = self.helper(root2,l1)
        print(li)
        print(l1)
        if l1==li:
            return True
        else:
            return False
