class Solution {
    public int numIslands(char[][] grid) {
        int count = 0; 
        int rows = grid.length; 
        int cols = grid[0].length; 
        for(int row = 0; row < rows; row++){
            for(int col = 0; col < cols; col++){
                if(grid[row][col] == '1'){
                    dfs(grid, row, col, rows, cols);

                    count++;
                }
                else{
                    continue;
                }
            }
        }
        return count;
    }

    private void dfs(char[][] grid, int row, int col, int rows, int cols){
        if(row < 0 || row >= rows){
            return;
        }
        if(col < 0 || col >= cols){
            return;
        }
        if(grid[row][col] == '0'){
            return;
        }
        else{
            grid[row][col] = '0';

            dfs(grid, row + 1, col, rows, cols);
            dfs(grid, row - 1, col, rows, cols);
            dfs(grid, row, col + 1, rows, cols);
            dfs(grid, row, col - 1, rows, cols);
        }
    }
}
