class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length; 
        for(int i = 0; i < rows; i++){
            if(target >= matrix[i][0] && target <= matrix[i][cols - 1]){
                return binarySearch(matrix[i], target);
            }
        }
        return false;
    }

    private boolean binarySearch(int[] array, int target){
        int start = 0;
        int end = array.length;
        while(start <= end){
            int mid = (start + end) / 2;
            if(array[mid] == target){
                return true;
            }
            else if(array[mid] > target){
                end = mid - 1;
            }
            else if(array[mid] < target){
                start = mid + 1;
            }
        }
        return false;
    }
}
