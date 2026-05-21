class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for(int i = 0; i < nums.length; i++){
            minHeap.offer(nums[i]);
        }
        int loops = nums.length - k;
        int j = 0;
        while(j < loops){
            minHeap.poll();
            j++;
        }
        return minHeap.peek();
    }
}
