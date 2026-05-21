class Solution {
    public String minWindow(String s, String t) {
        String ans = "";
        int current = Integer.MAX_VALUE;
        char[] sArray = s.toCharArray();
        Map<Character, Integer> tMap = new HashMap<>();
        Map<Integer, String> storeAns = new HashMap<>();

        for(char c : t.toCharArray()){
            tMap.put(c, tMap.getOrDefault(c, 0) + 1);
        }
        
        for(int i = 0; i < sArray.length; i++){
            for(int j = i + 1; j <= sArray.length; j++){
                if(isValid(s.substring(i, j), tMap)){
                    storeAns.put((j - i), s.substring(i, j));
                }
            }
        }
        for(Map.Entry<Integer, String> entry : storeAns.entrySet()){
            System.out.println(entry);
            if(entry.getKey() < current){
                ans = entry.getValue();
                current = entry.getKey();
            }
        }
        return ans;
    }

    private boolean isValid(String s, Map<Character, Integer> tMap) {
    Map<Character, Integer> tempMap = new HashMap<>();
    for (char c : s.toCharArray()) {
        tempMap.put(c, tempMap.getOrDefault(c, 0) + 1);
    }

    for (Map.Entry<Character, Integer> entry : tMap.entrySet()) {
        char key = entry.getKey();
        int requiredCount = entry.getValue();
        if (tempMap.getOrDefault(key, 0) < requiredCount) {
            return false;
        }
    }

    return true;
}

}
