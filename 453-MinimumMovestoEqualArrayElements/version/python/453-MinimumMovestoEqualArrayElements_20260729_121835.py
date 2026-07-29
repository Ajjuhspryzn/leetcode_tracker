# Last updated: 7/29/2026, 12:18:35 PM
1class Solution(object):
2    def minMoves(self, nums):
3        nm=min(nums)
4        total=0
5        for x in nums:
6            total+=x-nm
7        return total