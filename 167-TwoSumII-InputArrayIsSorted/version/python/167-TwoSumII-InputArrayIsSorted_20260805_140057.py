# Last updated: 8/5/2026, 2:00:57 PM
1class Solution(object):
2    def twoSum(self, numbers, target):
3        left=0
4        right=len(numbers)-1
5        sum=0
6        while left<right:
7            sum=numbers[left]+numbers[right]
8            if sum==target:
9                return[left+1,right+1]
10            elif sum<target:
11                left+=1
12            else:
13                right-=1
14        