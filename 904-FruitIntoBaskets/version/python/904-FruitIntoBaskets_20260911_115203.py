# Last updated: 9/11/2026, 11:52:03 AM
1class Solution:
2    def totalFruit(self, fruits: list[int]) -> int:
3        left = 0
4        basket = {}
5        ans = 0
6
7        for right in range(len(fruits)):
8            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
9
10            while len(basket) > 2:
11                basket[fruits[left]] -= 1
12
13                if basket[fruits[left]] == 0:
14                    del basket[fruits[left]]
15
16                left += 1
17
18            ans = max(ans, right - left + 1)
19
20        return ans