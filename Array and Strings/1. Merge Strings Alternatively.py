'''
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

'''

class Solution(object):
    def mergeAlternately(self, word1, word2):
        n = len(word1)
        m = len(word2)
        i,j = 0,0
        l = 1
        s = ''
        k = min(n,m)
        for i in range(k):
            s+=word1[i]
            s+=word2[i]
        if n>m:
            s+=str(word1[i+1:])
        else:
            s+=str(word2[i+1:])
        return s
