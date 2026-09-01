# Last updated: 9/1/2026, 12:06:57 PM
1class TimeMap:
2
3    def __init__(self):
4        self.dic = {}
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        if key not in self.dic:
8            self.dic[key] = []
9        self.dic[key].append([value , timestamp])
10
11    def get(self, key: str, timestamp: int) -> str:
12        res = ""
13        values = self.dic.get(key , [])
14        l , r = 0 , len(values) - 1
15        while l <= r :
16            mid = (l + r) >> 1
17            if values[mid][1] <= timestamp:
18                l = mid + 1
19                res = values[mid][0]
20            else:
21                r = mid - 1
22        return res
23
24
25# Your TimeMap object will be instantiated and called as such:
26# obj = TimeMap()
27# obj.set(key,value,timestamp)
28# param_2 = obj.get(key,timestamp)