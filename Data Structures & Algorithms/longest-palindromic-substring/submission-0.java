class Solution {
    public String longestPalindrome(String s) {
        char[] charArray = s.toCharArray();
        Map<String, Integer> map = new HashMap<>();
        if(charArray.length == 0){
            return "";
        }
        if(charArray.length == 1){
            return s;
        }
        for(int i = 0; i < charArray.length; i++){
            for(int j = i+1; j <= charArray.length; j++){
                if(isValidPalindrome(s.substring(i, j))){
                    String substring = s.substring(i, j);
                    map.put(substring, substring.length());
                }
            }
        }
        String ans = "";
        int max = 0;
        for(Map.Entry<String, Integer> entry : map.entrySet()){
            if(entry.getValue() > max){
                ans = entry.getKey();
                max = entry.getValue();
            }
        }
        return ans;
    }
    private boolean isValidPalindrome(String s){
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
