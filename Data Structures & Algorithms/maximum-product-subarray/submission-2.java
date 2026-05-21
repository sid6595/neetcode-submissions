class Solution {
    public int maxProduct(int[] nums) {
        int[] maxProd = new int[nums.length];
        int[] minProd = new int[nums.length];
        if(nums.length == 1){
            return nums[0];
        }
        maxProd[0] = nums[0];
        minProd[0] = nums[0];
        int result = 0;
        for(int i = 1; i < nums.length; i++){
            maxProd[i] = Math.max(nums[i], Math.max(nums[i] * maxProd[i-1], nums[i] * minProd[i-1]));
            minProd[i] = Math.min(nums[i], Math.min(nums[i] * maxProd[i-1], nums[i] * minProd[i-1]));
            result = Math.max(result, maxProd[i]);
        }
        return result;
    }
}
