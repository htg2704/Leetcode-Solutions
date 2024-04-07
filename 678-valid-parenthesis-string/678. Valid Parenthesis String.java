class Solution {
    public boolean checkValidString(String s) {
        int l=0, r=0;
        for(char c: s.toCharArray()){
            if(c=='('){
                l+=1;
            }
            else{
                l-=1;
            }
            if(c!=')'){
                r+=1;
            }
            else{
                r-=1;
            }

            if(r<0) return false;
            l=Math.max(l,0);

        }
        return l==0;
    }
}