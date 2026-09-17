# Last updated: 9/17/2026, 11:05:13 AM
1class Solution:
2    def longestValidParentheses(self, s: str) -> int:
3        stack=[-1]
4        ans=0
5        for i in range(len(s)):
6            if s[i]=='(':
7                stack.append(i)
8            else:
9                stack.pop()
10            if not stack:
11                stack.append(i)
12            else:
13                ans=max(ans,i-stack[-1])
14        return ans