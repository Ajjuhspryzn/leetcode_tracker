# Last updated: 8/5/2026, 2:13:27 PM
1class Solution:
2    def countArrangement(self, n: int) -> int:
3        
4        nums = list(range(1, n+1))
5        self.count = 0
6        
7        def backtrack(start):
8    
9            if start == n:
10                self.count += 1
11            
12            for i in range(start, n):
13                
14                nums[start], nums[i] = nums[i], nums[start]
15            
16                if nums[start] % (start+1) == 0 or (start+1) % nums[start] == 0:
17                    
18                    backtrack(start+1)
19            
20                nums[start], nums[i] = nums[i], nums[start]
21        
22        
23        backtrack(0)
24        return self.count