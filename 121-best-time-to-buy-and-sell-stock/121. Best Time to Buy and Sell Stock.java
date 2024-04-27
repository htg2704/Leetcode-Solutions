class Solution {
    public int maxProfit(int[] prices) {

        int n = prices.length;
        int m = prices[0];
        int ans=0;
        for(int i=1;i<n;i++){
            ans = Math.max(ans, prices[i]-m);
            m = Math.min(m, prices[i]);
        }
        return ans;
    }
}