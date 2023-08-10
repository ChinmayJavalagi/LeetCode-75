'''
Input: s = "the sky is blue"
Output: "blue is sky the"
'''

class Solution(object):
    def reverseWords(self, s):
        li = s.split()
        li.reverse()
        return " ".join(li)
