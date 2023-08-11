# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def goodNodes(self, root):
        def helper(root,val,c):
            if root==None:
                return 
            if root.val>=val:
                c[0]+=1
                print(c[0])
            helper(root.left,max(root.val,val),c)
            helper(root.right,max(root.val,val),c)
            print(c[0])
            return c
        if root==None:
            return 0
        c = [0]
        helper(root,root.val,c)
        return c[0]
