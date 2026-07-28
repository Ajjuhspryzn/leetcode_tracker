# Last updated: 7/28/2026, 2:06:19 PM
1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3        A,B=len(word1),len(word2) 
4        a,b=0,0
5        word=1
6        s=[]
7        while a<A and b<B:
8            if word==1:
9                s.append(word1[a])
10                a+=1
11                word=2
12            else:
13                s.append(word2[b])
14                b+=1
15                word=1
16        while a<A:
17            s.append(word1[a])
18            a+=1
19            word=1
20        while b<B:
21            s.append(word2[b])
22            b+=1
23            word=1
24        
25        return ''.join(s)  
26            