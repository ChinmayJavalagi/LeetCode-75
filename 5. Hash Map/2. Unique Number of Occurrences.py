'''
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
'''

class Solution(object):
    def uniqueOccurrences(self, arr):
        d = {}
        for num in arr:
            if num in d:
                d[num]+=1
            else:
                d[num] = 1
        
        nums = [x for x in d.values()]
        return len(nums)==len(set(nums))
