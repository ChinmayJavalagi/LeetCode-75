# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        q = deque()
        q.append(root)
        s = 0
        level = 0
        m = float("-inf")
        l = 1
        while q:
            s = 0
            n = len(q)
            for i in range(n):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s>m:
                m = s
                level = l
            l+=1
        return level
