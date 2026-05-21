class Solution {

    public String encode(List<String> strs) {
        StringBuilder builder = new StringBuilder();
        for(String s : strs){
            builder.append(s.length()).append('#').append(s);
        }
        return builder.toString();
    }

    public List<String> decode(String str) {
        List<String> ans = new ArrayList<>();
        int i = 0;

        while (i < str.length()) {
            int j = i;
            // 1) scan forward to find the '#'
            while (str.charAt(j) != '#') {
                j++;
            }
            // 2) parse length from [i, j)
            int length = Integer.parseInt(str.substring(i, j));
            // 3) read exactly 'length' chars after '#'
            int start = j + 1;
            int end = start + length; // exclusive
            ans.add(str.substring(start, end));
            // 4) move i to the next chunk
            i = end;
        }
        return ans;
    }
}
