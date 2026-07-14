// Last updated: 7/14/2026, 3:20:09 PM
class Solution {
    public int climbStairs(int n) {
        if(n==1)
          return 1;

          int fst=1;
          int second=2;
        for(int i=3;i<=n;i++){
        int third=fst+second;
        
        fst=second;
        second=third;
        }
        return second;
    }
}