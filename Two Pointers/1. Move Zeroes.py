'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Solution(object):
    def moveZeroes(self, nums):
        if len(nums)==1:
            return nums
        l,r = 0,0
        while l<len(nums) and r<len(nums):
            if nums[r]!=0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r+=1
            else:
                r+=1
        return nums
            
