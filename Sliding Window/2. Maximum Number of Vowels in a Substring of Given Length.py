'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

'''

class Solution(object):
    def maxVowels(self, s, k):
        m = 0
        c = 0
        li = ['a','e','i','o','u']
        for i in range(k):
            if s[i] in li:
                c+=1
        m = c
        for i in range(k,len(s)):
            if s[i-k] in li:
                c-=1
            if s[i] in li:
                c+=1
            m = max(m,c)
        return m
