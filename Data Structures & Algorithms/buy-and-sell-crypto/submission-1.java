class Solution {
    public int maxProfit(int[] prices) {
        int start = prices[0];
        int profit = 0;
        for(int i = 1; i < prices.length; i++){
            if(prices[i] < start){
                start = prices[i];
            }
            else{
                if(prices[i] - start > profit){
                    profit = prices[i] - start;
                }
            }
        }
        return profit;
    }
}
