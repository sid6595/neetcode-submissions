class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        int max = 0;
        for(int n : set){
            if(!set.contains(n - 1)){
                int length = 1;
                int current = n;

                while(set.contains(current + 1)){
                length++;
                current++;
                }
                max = Math.max(max, length);
            }
        }
        return max;
    }
}

