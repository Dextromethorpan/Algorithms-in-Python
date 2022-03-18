"""
Merge Intervals

Given a collection of intervals, merge all overlapping intervals
Input:[[1,3],[2,6],[8,10],[15,18]]
Output:[[1,6],[8,10],[15,18]]

"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]])->List[List[int]]:
        def takeFirst(elem):
            return elem[0]
        intervals.sort(key=takeFirst)
        res=[]
        for interval in intervals:
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1]=max(res[-1][1],interval[1])
        return res 

