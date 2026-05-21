/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    List<List<Integer>> ans = new ArrayList<>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if(root == null){
            return ans;
        }
        Queue<TreeNode> nodes = new LinkedList<>();
        nodes.add(root);
        int size = nodes.size();
        while(!nodes.isEmpty()){
            List<Integer> inner = new ArrayList<>();
            for(int i = 0; i < size; i++){
                TreeNode curr = nodes.poll();
                if(curr == null){
                    continue;
                }
                inner.add(curr.val);
                nodes.add(curr.left);
                nodes.add(curr.right);
            }
            if(inner.size() > 0){
                ans.add(inner);
            }
            size = nodes.size();
        }
        return ans;
    }
}
