# Last updated: 8/22/2026, 12:40:56 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def deleteNode(self, root, key):
9        if not root: return None
10        if root.val==key:
11            if not root.right: return root.left
12            if not root.left: return root.right
13            if root.left and root.right:
14                temp=root.right
15                while temp.left: temp = temp.left
16                root.val=temp.val
17                root.right=self.deleteNode(root.right,root.val)
18        elif root.val>key:
19            root.left=self.deleteNode(root.left,key)
20        else:
21            root.right=self.deleteNode(root.right,key)
22        return root
23
24        