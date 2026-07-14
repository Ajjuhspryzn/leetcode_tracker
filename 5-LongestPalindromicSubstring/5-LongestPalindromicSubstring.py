# Last updated: 7/14/2026, 3:21:15 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):

                sub = s[i:j+1]

                if sub == sub[::-1]:
                    if len(sub) > len(longest):
                        longest = sub

        return longest