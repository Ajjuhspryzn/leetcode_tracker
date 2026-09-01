# Last updated: 9/1/2026, 10:35:45 AM
1class Solution(object):
2    def findingUsersActiveMinutes(self, logs, k):
3        users={}
4        for user, minutes in logs:
5            if user not in users:
6                users[user]=set()
7            users[user].add(minutes)
8        ans=[0]*k
9        for minutes in users.values():
10            ans[len(minutes)-1]+=1
11        return ans
12