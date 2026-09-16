# Last updated: 9/16/2026, 4:02:21 PM
1class Solution:
2    def preorderTraversal(self, root):
3        ret = []
4        stack = [root]
5        while stack:
6            node = stack.pop()
7            if node:
8                ret.append(node.val)
9                stack.append(node.right)
10                stack.append(node.left)
11        return ret