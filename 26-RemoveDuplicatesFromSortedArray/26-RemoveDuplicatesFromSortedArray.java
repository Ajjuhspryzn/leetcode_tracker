// Last updated: 7/14/2026, 3:20:48 PM
class Solution {
    public int removeDuplicates(int[] arr) {
      int i=0;
      for(int j=1;j<arr.length;j++){
        if(arr[i]!=arr[j]){
            i++;
            arr[i]=arr[j];
        }
      }  
      return i+1;
    }
}