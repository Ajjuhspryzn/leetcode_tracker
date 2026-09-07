# Last updated: 9/7/2026, 12:03:42 PM
1class Solution:
2    def maxProfit(self, prices):
3        buy1 = float('-inf')
4        sell1 = 0
5        buy2 = float('-inf')
6        sell2 = 0
7
8        for price in prices:
9            buy1 = max(buy1, -price)
10            sell1 = max(sell1, buy1 + price)
11
12            buy2 = max(buy2, sell1 - price)
13            sell2 = max(sell2, buy2 + price)
14
15        return sell2