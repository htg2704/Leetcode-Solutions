class Solution {
    public int lengthOfLastWord(String s) {
        int n = s.length()-1;
        while(s.charAt(n)==' '){
            n--;
        }
        int ans=0;
        for(int i=n;i>=0;i--){
            if(s.charAt(i)==' '){
                return ans;
            }
            ans++;
        }
        return ans;
    }
}