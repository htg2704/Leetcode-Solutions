class Solution {
    public List<Integer> spiralOrder(int[][] a) {
        int m = a.length;
        int n = a[0].length;
        List<Integer> ans =  new ArrayList<>();
        int l=0, r=n-1, t=0, b=m-1;
        while(l<=r && t<=b){
            for(int i=l;i<=r;i++){
                ans.add(a[t][i]);
            }
            t++;
            for(int i=t;i<=b;i++){
                ans.add(a[i][r]);
            }
            r--;
            if(t<=b){
            for(int i=r;i>=l;i--){
                ans.add(a[b][i]);
            }
            b--;
            }
            if(l<=r){
            for(int i=b;i>=t;i--){
                ans.add(a[i][l]);
            }
            l++;
            }
        }
        return ans;
    }
}