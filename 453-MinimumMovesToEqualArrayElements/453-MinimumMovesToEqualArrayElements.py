# Last updated: 8/4/2026, 12:29:29 PM
class Solution(object):
    def minMoves(self, nums):
        nm=min(nums)
        total=0
        for x in nums:
            total+=x-nm
        return total