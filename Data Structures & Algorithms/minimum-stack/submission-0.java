class MinStack {

    private Stack<Integer> minStack = new Stack<>();

    public MinStack() {
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        minStack.push(val);
    }
    
    public void pop() {
        minStack.pop();
    }
    
    public int top() {
       return minStack.peek();
    }
    
    public int getMin() {
        int min = (int) Math.pow(2,31);
        for(Integer num : minStack){
            if(num < min){
                min = num;
            }
        }
        return min;
    }
}
