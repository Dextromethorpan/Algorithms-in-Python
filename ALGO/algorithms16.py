"""
Sum of Squares

Given a number n, find the least number of squares needed to sum up to the number.

Here's an example and some starting code

Example:
Input:13
13=3^2+2^2
Output:2
"""

def square_sum(n):
    squares=[]
    i=1
    while i*i<n: #O(sqr(n))
        squares.append(i*i)
        i += 1
    
    mins_sums=[n]*(n+1) #with this, at least we know that the maximum number is the sum of 1^2.
    mins_sums[0]=0

    for idx in range(len(mins_sums)):
        for s in squares:
            if idx + s < len(mins_sums):
                mins_sums[idx+s]=min(mins_sums[idx+s],mins_sums[idx]+1)
    return mins_sums[-1]