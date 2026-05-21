class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        int[] ans = new int[k];
        for(int i = 0; i < nums.length; i++){
            counts.put(nums[i], counts.getOrDefault(nums[i], 0) + 1);
        }
        int i = 0;
        while(i < k){
            int maxFreq = 0;
            int maxKey = 0;
            for(Map.Entry<Integer, Integer> entry : counts.entrySet()){
                int currentFreq = entry.getValue();
                if(currentFreq > maxFreq){
                    maxKey = entry.getKey();
                    maxFreq = currentFreq;
                }
            }
            System.out.println(maxKey);
            System.out.println(maxFreq);
            ans[i] = maxKey;
            counts.remove(maxKey);
            i++;
        }
        return ans;
    }
}
