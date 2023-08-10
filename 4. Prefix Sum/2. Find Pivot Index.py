'''
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
'''

class Solution(object):
    def pivotIndex(self, nums):
        ind = -1
        pre = [0]*(len(nums)+1)
        post = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            pre[i] = pre[i-1]+nums[i-1]
        for i in range(len(nums)-1,0,-1):
            post[i] = post[i+1]+nums[i]
        for i in range(1,len(nums)+1):
            if pre[i-1]==post[i]:
                ind = i-1
                break
        print(pre)
        print(post)
        return ind
