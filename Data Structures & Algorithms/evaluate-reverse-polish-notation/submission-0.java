class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String s : tokens){
            if(isOperator(s)){
                int first = stack.pop();
                int second = stack.pop();
                int pushed = operate(second, first, s);
                stack.push(pushed);
            }
            else{
                stack.push(Integer.valueOf(s));
            }
        }
        return stack.peek();
    }   

    public boolean isOperator(String s){
        return s.equals("+") || s.equals("-") || s.equals("/") || s.equals("*");
    }

    public int operate(int first, int second, String operator){
        int ans = 0;
        if(operator.equals("+")){
            ans = first + second;
        }
        if(operator.equals("-")){
            ans = first - second;
        }
        if(operator.equals("/")){
            ans = first / second;
        }
        if(operator.equals("*")){
            ans = first * second;
        }
        return ans;
    }
}
