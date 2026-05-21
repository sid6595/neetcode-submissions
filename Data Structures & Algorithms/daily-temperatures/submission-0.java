class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] results = new int[temperatures.length];
        for(int i = 0; i < temperatures.length; i++){
            results[i] = 0;
            for(int j = i+1; j < temperatures.length; j++){
                if(temperatures[j]  > temperatures[i]){
                    results[i] = j - i;
                    break;
                }
            }
        }
        return results;
    }
}
