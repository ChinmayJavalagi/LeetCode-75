'''
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
'''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        
        def divisor(l):
            if len1%l or len2%l:
                return False
            f1,f2 = len1//l , len2//l
            return str2[0:l]*f1 == str1 and str2[0:l]*f2 == str2
        for l in range(min(len1,len2),0,-1):
            if divisor(l):
                return str2[:l]
        return ""

        
