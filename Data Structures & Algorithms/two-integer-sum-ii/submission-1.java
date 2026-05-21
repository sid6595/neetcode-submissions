class Solution {
    public int[] twoSum(int[] numbers, int target) {
        ArrayList<Integer> list = new ArrayList<>();
        int[] ans = new int[2];
        for(int i = 0; i < numbers.length; i++){
            list.add(numbers[i]);
        }
        for(int i = 0; i < list.size(); i++){
            int diff = target - list.get(i);
            if(list.contains(diff) && i != list.indexOf(diff)){
                int second = list.indexOf(diff);
                ans[0] = Math.min(i + 1, second + 1);
                ans[1] = Math.max(i + 1, second + 1);
                break;
            }
        }
        return ans;
    }
}
