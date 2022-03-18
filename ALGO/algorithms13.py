"""
Product of Array Except Self

Given an array nums of n integers where n>1, return an array 
output such that output[i] is equal to the product of
all the elements of nums except nums[i]

Example:
Input: [1,2,3,4]
Output: [24,12,8,6]

"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int])->List[int]:
        res=[1]*len(nums)
        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i-1]
        right=1
        for i in range(len(nums)-2,-1,-1): 
            right*=nums[i+1]
            res[i]*=right
        return res

