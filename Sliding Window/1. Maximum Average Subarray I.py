'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        if len(nums)<k:
            return 0
        m = float('-inf')
        avg = 0
        for i in range(k):
            avg+= nums[i]
        print(m)
        m = max(m,avg)
        for i in range(k,len(nums)):
            avg = avg-(nums[i-k])+(nums[i])
            m = max(m,avg)
        return m/float(k)
