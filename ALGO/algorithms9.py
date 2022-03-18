"""
Minimum Size Subarray Sum 

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
which the sum > s. If there isn't one, return 0 instead.

Example:
Input: s=7, nums=[2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal lenght under the problem constraint.

"""
from typing import List


class Solution:
    def minSubArrayLen(self,s:int, nums: List[int])->int:
        res=float('inf')
        sum=0
        left=0
        right=0
        while right<len(nums):
            sum +=nums[right]
            while sum >= s:
                #updating the result 
                res=min(res,right-left +1)
                #increment left pointer
                sum -=nums[left]
                left +=1.
            #increment right pointer
            right +=1
        if res == float('inf'):
            return 0
        else:
            return res
