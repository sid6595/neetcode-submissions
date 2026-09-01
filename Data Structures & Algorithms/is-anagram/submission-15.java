class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        Map<Character, Integer> map1 = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            char first = s.charAt(i);
            char second = t.charAt(i);
            map1.put(first, map1.getOrDefault(first, 0) + 1);
            map2.put(second, map2.getOrDefault(second, 0) + 1);
        }
        return map1.equals(map2);
    }
}
