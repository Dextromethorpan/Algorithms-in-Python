"""
Permutations 

Given a collection of distinct integers, return all possible permutations.

Input: [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[,3,1,2],[3,2,1]]

"""
from typing import List

class Solution:
    def permute(self, nums:List[int])->List[List[int]]:
        res=[]
        def permuteHelper(start):
            if start==len(nums)-1:
                res.append(nums.copy())
            for i in range(start,len(nums)):
                nums[start],nums[i]=nums[i],nums[start]
                permuteHelper(start+1)
                nums[start],nums[i]=nums[i],nums[start]
        permuteHelper(0)                  
        return res
