# Last updated: 9/12/2026, 11:57:19 AM
1class Solution(object):
2    def numberOfSubarrays(self, nums, k):
3        n = len(nums)
4        cnt = [0] * (n + 1)
5        cnt[0] = 1
6        ans = 0
7        t = 0
8        for v in nums:
9            t += v & 1
10            if t - k >= 0:
11                ans += cnt[t - k]
12            cnt[t] += 1
13        return ans
14        
15        