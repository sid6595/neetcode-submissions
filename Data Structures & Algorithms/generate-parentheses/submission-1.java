class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        backtrack(0, 0, n, ans, sb);
        return ans;
    }

    private void backtrack(int open, int close, int n, List<String> ans, StringBuilder sb){
        if(open == close && open == n){
            ans.add(sb.toString());
            return;
        }
        if(open < n){
            sb.append('(');
            backtrack(open + 1, close, n, ans, sb);
            sb.deleteCharAt(sb.length() - 1);
        }
        if(close < open){
            sb.append(')');
            backtrack(open, close + 1, n, ans, sb);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
