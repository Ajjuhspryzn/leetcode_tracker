# Last updated: 7/29/2026, 11:57:34 AM
1class Solution(object):
2    def findMaxLength(self, nums):
3        d={0:-1}
4        s=0
5        ans=0
6        for i in range(len(nums)):
7            if nums[i]==0:
8                s-=1
9            else:
10                s+=1
11            if s in d:
12                ans=max(ans,i-d[s])
13            else:
14                d[s]=i
15        return ans
16         
17        