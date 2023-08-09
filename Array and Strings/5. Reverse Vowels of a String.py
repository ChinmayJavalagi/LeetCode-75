'''
Input: s = "hello"
Output: "holle"

'''
class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        li = set(['a','e','i','o','u','A','E','I','O','U'])
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] in li and s[r] in li:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
            while s[l] not in li and l<len(s)-1:
                l+=1
            while s[r] not in li and r>0:
                r-=1
            # if s[l] not in li and s[r] not in li:
                # l+=1
                # r-=1
        return "".join(s)
        
