# Last updated: 9/16/2026, 4:05:11 PM
1class Solution:
2    def majorityElement(self, nums: list[int]) -> int:
3        nums.sort()
4        n=len(nums)
5        return nums[n//2]