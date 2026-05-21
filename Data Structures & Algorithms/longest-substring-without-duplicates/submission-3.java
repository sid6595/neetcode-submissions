class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() == 1){
            return 1;
        }
        int max = 0;
        char[] array = s.toCharArray(); 
        for(int i = 0; i < array.length; i++){
            HashSet<Character> set = new HashSet<>();
            set.add(array[i]);
            int count = 1;
            for(int j = i + 1; j < array.length; j++){
                if(set.contains(array[j])){
                    break;
                }
                else{ 
                    count++;
                    set.add(array[j]);
                }
            }
            max = Math.max(max, count);
        }
        return max;
    }
}
