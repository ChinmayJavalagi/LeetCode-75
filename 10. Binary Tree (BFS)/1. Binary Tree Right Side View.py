# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rightSideView(self, root):
        if root == None:
            return []
        q = deque()
        li = []
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i==(n-1):
                    li.append(node.val)
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
        return li
