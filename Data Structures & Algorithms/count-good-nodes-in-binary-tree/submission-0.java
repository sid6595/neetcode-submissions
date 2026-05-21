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
    int count = 0;
    public int goodNodes(TreeNode root) {
        if(root == null){
            return 0;
        }
        else{
            dfs(root, root.val);            
        }
        return count;
    }

    public void dfs(TreeNode root, int maxValue){
        if(root == null){
            return;
        }
        if(root.val >= maxValue){
            count++;
            maxValue = root.val;
        }
        dfs(root.left, maxValue);
        dfs(root.right, maxValue);
    }
}
