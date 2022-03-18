"""
Maximum Subarray 

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest 
sum and return its sum.

Example: 
    Input: [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6

"""

from typing import List


class Solution:
    def maxSubArray(self,nums:List[int])->int:
        if len(nums)==0:
            return 0
        res=nums[0]
        currMax=0
        for n in nums:
            if currMax + n<0:
                currMax=0
                res=max(n,res)
            else:
                currMax += n 
                res=max(currMax,res)
        return res 