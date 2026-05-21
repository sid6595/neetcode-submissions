class Solution {
    public int countSubstrings(String s) {
        ArrayList<String> palindromes = new ArrayList<>();
        char[] charArray = s.toCharArray();
        if(charArray.length == 0){
            return 0;
        }
        if(charArray.length == 1){
            return 1;
        }
        for(int i = 0; i < charArray.length; i++){
            for(int j = i + 1; j <= charArray.length; j++){
                String substring = s.substring(i, j);
                if(isValidPalindrome(substring)){
                    palindromes.add(substring);
                }
            }
        }
        return palindromes.size();
    }
    private boolean isValidPalindrome(String s){
        if(s.length() == 1){
            return true;
        }
        int l = 0;
        int r = s.length() - 1;
        while(l < r){
            if(s.charAt(l) == s.charAt(r)){
                l++;
                r--;
            }
            else{
                return false;
            }
        }
        return true;
    }
}
