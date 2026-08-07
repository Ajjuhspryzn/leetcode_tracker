# Last updated: 8/7/2026, 4:01:32 PM
1class Solution(object):
2    def isPalindrome(self, s):
3        cleaned=re.sub(r'[^a-zA-Z0-9]','',s).lower()
4        return cleaned==cleaned[::-1]
5              