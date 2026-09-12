# Last updated: 9/12/2026, 12:38:56 PM
1class Solution:
2    def maximumUniqueSubarray(self, nums: List[int]) -> int:
3        res = 0
4        cur_sum = 0
5        start = 0
6        seen = set()
7
8        for end in range(len(nums)):
9            while nums[end] in seen:
10                seen.remove(nums[start])
11                cur_sum -= nums[start]
12                start += 1
13
14            cur_sum += nums[end]
15            seen.add(nums[end])
16
17            res = max(res, cur_sum)
18
19        return res