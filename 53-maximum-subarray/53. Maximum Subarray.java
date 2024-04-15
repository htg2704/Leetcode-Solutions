class Solution {
    public int maxSubArray(int[] nums) {
        int sum = 0;
        int max_sum = nums[0];
        for(int i: nums){
            sum+=i;
            if(max_sum<sum) max_sum=sum;
            if(sum<0) sum=0;
        }
        return max_sum;
    }
}