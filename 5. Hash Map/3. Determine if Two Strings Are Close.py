'''
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
'''

class Solution(object):
    def closeStrings(self, word1, word2):
        if set(word1)!=set(word2):
            return False

        li1,li2 = [],[]
        for i in set(word1):
            li1.append(list(word1).count(str(i)))
        for i in set(word2):
            li2.append(list(word2).count(str(i)))
        if sorted(li1)==sorted(li2):
            return True
