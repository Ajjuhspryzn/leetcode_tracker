# Last updated: 8/7/2026, 11:54:55 AM
1class Solution:
2    def isValidSerialization(self, preorder: str) -> bool:
3
4        slots = 1
5        for node in preorder.split(','):
6            slots-=1
7            if slots<0:
8                return False
9            if node!="#":
10                slots+=2
11        return slots==0
12            