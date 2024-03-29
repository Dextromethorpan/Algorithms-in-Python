"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of 
the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0,1 and 2 to represent the color red, white and blue respectively.

Note: You are not suppose to use the library's sore function for this problem.

Example:
    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p0=0
        p1=0
        p2=len(nums)-1

        while p1<=p2:
            if nums[p1]==0:
                nums[p0],nums[p1]=nums[p1],nums[p0]
                p0 += 1
                p1 += 1
            elif nums[p1]==1:
                p1 += 1
            else:
                nums[p0],nums[p2]=nums[p2],nums[p0]
                p2 -= 1

