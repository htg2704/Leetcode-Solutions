class Solution {
    public int majorityElement(int[] nums) {
        int n = nums.length,c=0,ans=0;
        for(int i=0; i<n;i++){
            if(c==0){
                c++;
                ans=nums[i];
            }
            else if(nums[i]==ans){
                c++;
            }
            else
                c--;
        }
        return ans;
    }
}