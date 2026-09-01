class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }
        for(int j = 0; j < nums.length; j++){
            int diff = target - nums[j];
            if(map.containsKey(diff) && map.get(diff) != j){
                ans[0] = j;
                ans[1] = map.get(diff);
                break;
            }
        }
        return ans;
    }
}
