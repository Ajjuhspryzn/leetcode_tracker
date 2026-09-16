# Last updated: 9/16/2026, 3:58:40 PM
1class Solution:
2    def singleNumber(self, nums: list[int]) -> int:
3        xor=0
4        for num in nums:
5            xor^=num
6        return xor