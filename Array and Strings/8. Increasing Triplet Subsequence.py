'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
'''

class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums)<3:
            return False
        left, mid = float("inf"),float("inf")
        for i in nums:
            if i>mid:
                return True
            elif(i>left and i<mid):
                mid = i
            elif i<left:
                left = i
        return False
