# Last updated: 9/11/2026, 12:40:09 PM
1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        left=0
4        zero=0
5        ans=0
6        for right in range(len(nums)):
7            if nums[right]==0:
8                zero+=1
9            while zero>k:
10                if nums[left]==0:
11                    zero-=1
12                left+=1
13            ans=max(ans,right-left+1)
14        return ans