class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Set<Integer> visited = new HashSet<>();
        List<List<String>> outer = new ArrayList<>();
        for(int i = 0; i < strs.length; i++){
            if(visited.contains(i)){
                continue;
            }
            visited.add(i);
            List<String> inner = new ArrayList<>();
            inner.add(strs[i]);
            for(int j = i + 1; j < strs.length; j++){
                if(isAnagram(strs[i], strs[j])){
                    visited.add(j);
                    inner.add(strs[j]);
                }
            }
            outer.add(inner);
        }
        return outer;
    }

    private boolean isAnagram(String str1, String str2){
        Map<Character, Integer> map1 = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();
        for(int i = 0; i < str1.length(); i++){
            char c = str1.charAt(i);
            map1.put(c, map1.getOrDefault(c, 0) + 1);
        }
        for(int j = 0; j < str2.length(); j++){
            char c = str2.charAt(j);
            map2.put(c, map2.getOrDefault(c, 0) + 1);
        }
        if(map1.equals(map2)){
            return true;
        }
        else{
            return false;
        }
    }
}
