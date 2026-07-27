# Last updated: 7/27/2026, 3:49:16 PM
class Solution(object):
    def findClosestNumber(self, nums):
        closest=nums[0]
        for x in nums:
            if abs(x)<abs(closest):
                closest=x
        if closest<0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        