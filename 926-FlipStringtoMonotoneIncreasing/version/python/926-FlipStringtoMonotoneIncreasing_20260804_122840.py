# Last updated: 8/4/2026, 12:28:40 PM
1class Solution(object):
2    def minFlipsMonoIncr(self, s):
3        ones=0
4        flips=0
5        for ch in s:
6            if ch=="1":
7                ones+=1
8            else:
9                flips=min(flips+1,ones)
10        return flips
11