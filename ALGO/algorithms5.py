"""
Best Time to Buy and Sell Stock 

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transation (ie, buy one and sell one share of the stock),
design and algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit=6-1=5.
    Not 7-1=6, as selling price needs to be larger than buying price.
"""

class Solution():
    def maxProfit(self,prices):
        """
        :type prices: List[int]
        :rtype: int 
        """
        if prices == []:
            return 0
        res=0
        min=prices[0]
        for p in prices:
            if min>p:
                min=p
            res=max(res,p-min)
        return res

    # def prit(self):
    #     print("hola")
    
    #Si no paso self como argumento, recibo el Error que me falta un argumento
