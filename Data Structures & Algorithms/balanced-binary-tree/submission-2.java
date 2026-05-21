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
    public boolean isBalanced(TreeNode root) {
        if(root == null){
            return true;
        }
        int left = helper(root.left);
        int right = helper(root.right);
        if(Math.abs(left - right) > 1){
            return false;
        }
        return isBalanced(root.right) && isBalanced(root.left);
    }

    private int helper(TreeNode root){
        if(root == null){
            return 0;
        }
        int leftHeight = helper(root.left);
        int rightHeight = helper(root.right);
        int height = Math.max(leftHeight, rightHeight) + 1;
        return height;
    }
}
