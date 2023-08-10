'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Input: s = "abc", t = "ahbgdc"
Output: true
'''

class Solution(object):
    def isSubsequence(self, s, t):
        if not s and not t:
            return True
        if not t:
            return False
        if not s:
            return True
        
        l1,l2 = 0,0
        while l2<len(t)and l1<len(s):
            if s[l1]==t[l2]:
                l1+=1
                l2+=1
            else:
                l2+=1
        if l1==len(s):
            return True
        return False
