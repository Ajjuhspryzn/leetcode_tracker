# Last updated: 7/14/2026, 3:20:41 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=nums.index(target) if target in nums else -1
        return n