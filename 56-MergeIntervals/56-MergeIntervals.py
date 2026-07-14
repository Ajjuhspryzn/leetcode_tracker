# Last updated: 7/14/2026, 3:20:17 PM
class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        result=[]
        for interval in intervals:
            if not result or result[-1][1]<interval[0]:
                result.append(interval)
            else:
                result[-1][1]=max(result[-1][1],interval[1])
        return result