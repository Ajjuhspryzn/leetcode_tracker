# Last updated: 8/3/2026, 4:24:50 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
4        sum=0
5        n=len(s)
6        i=0
7        while i<n:
8            if i<n-1 and d[s[i]]<d[s[i+1]]:
9                sum+=d[s[i+1]]-d[s[i]]
10                i+=2
11            else:
12                sum+=d[s[i]]
13                i+=1
14        return sum