"""
Unique Path 

A robot is located at the top-left corner of a mxn grid (marked 'Start' in the diagram below). 
The robot can only move either down or right at any point in time. The robot is trying to reach 
the bottom-right corner of the grid (marked 'Finished'in the diagram below). 

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:
Input: m=3, n=2
Output: 3 
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1.Right->Right->Right
2.Right->Down->Right
3.Down->Right->Right
"""
class Solution:
    def uniquePaths(self, m:int,n:int)->int:
        matrix=[]
        for i in range(m):
            matrix.append([0]*n)
        for i in range(m):
            matrix[i][0]=1
        for j in range(n):
            matrix[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j]=matrix[i][j-1]+matrix[i-1][j]
        return matrix[m-1][n-1]

