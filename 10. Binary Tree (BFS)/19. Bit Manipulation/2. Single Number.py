class Solution(object):
    def singleNumber(self, nums):
        x = nums[0]
        for i in range(1,len(nums)):
            x = x^nums[i]
        return x
