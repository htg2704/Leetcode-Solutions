class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int n=nums.length;
        List<Integer> ans = new ArrayList<>();
        int c1=0, c2=0;
        int e1 = Integer.MIN_VALUE;
        int e2 = Integer.MIN_VALUE;
        for(int i=0; i<n;i++){
            if(c1==0 && nums[i]!=e2){
                c1++;
                e1=nums[i];
            } else if(c2==0 && nums[i]!=e1){
                c2++;
                e2=nums[i];
            }
            else if(nums[i]==e1){
                c1++;
            }
            else if(nums[i]==e2){
                c2++;
            }
            else{
                c1--;c2--;
            }
        }
        c1=0;
        c2=0;
        for(int i=0; i<n;i++){
            if(nums[i]==e1){
                c1++;
            } else if(nums[i]==e2){
                c2++;
            }
        }
        if(c1>n/3){
            ans.add(e1);
        }
        if(c2>n/3){
            ans.add(e2);
        }
        return ans;
    }
}