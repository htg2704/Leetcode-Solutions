class Solution {
    public int timeRequiredToBuy(int[] t, int k) {
        int n = t.length;
        int x = t[k];
        int time=0;
        for(int i=0; i<n;i++){
            if(i<k){
                time+=Math.min(t[i], x);
            } else if(i==k){
                time+=x;
            } else{
                if(t[i]<x)
                    time+=t[i];
                else
                    time+=x-1;
            }
        }
    return time;
    }
}