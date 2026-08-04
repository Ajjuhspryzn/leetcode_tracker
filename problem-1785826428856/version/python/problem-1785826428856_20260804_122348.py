# Last updated: 8/4/2026, 12:23:48 PM
1class Solution:
2    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
3        for i ,src,tg in sorted(list(zip(indices,sources,targets)),reverse=True):
4            if s[i:i+len(src)]==src:s=s[:i]+tg+s[i+len(src):]
5        return s