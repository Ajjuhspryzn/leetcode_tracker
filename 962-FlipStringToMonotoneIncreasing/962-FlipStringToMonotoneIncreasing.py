# Last updated: 8/4/2026, 12:29:14 PM
class Solution(object):
    def minFlipsMonoIncr(self, s):
        ones=0
        flips=0
        for ch in s:
            if ch=="1":
                ones+=1
            else:
                flips=min(flips+1,ones)
        return flips
