class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] ans = new int[k];
        for(int i = 0; i < nums.length; i++){
            int current = nums[i];
            map.put(nums[i], map.getOrDefault(current, 0) + 1);
        }
        int j = 0;
        while(j < k){
            int maxFreq = 0;
            int maxKey = 0;
            for(Map.Entry<Integer, Integer> entry : map.entrySet()){
                int currentValue = entry.getValue();
                
                if(currentValue > maxFreq){
                    maxFreq = currentValue;
                    maxKey = entry.getKey();
                }
            }
            ans[j] = maxKey;
            j++;
            map.remove(maxKey);
        }
        return ans;
    }
}
