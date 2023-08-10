'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

'''

class Solution(object):
    def maxOperations(self, nums, k):
        l,r = 0,len(nums)-1
        c = 0
        nums.sort()
        while l<r:
            if nums[l]+nums[r]==k:
                r-=1
                l+=1
                c+=1
            elif nums[l]+nums[r]>k:
                r-=1
            else:
                l+=1
        return c
