class Solution {
    public int countPaths(int[][] grid) {
        int[][] visited = new int[grid.length][grid[0].length];
        return dfs(grid, 0, 0, visited);
    }
    private int dfs(int[][] grid, int row, int col, int[][] visited){
        int Row = grid.length;
        int Col = grid[0].length;
        if(Math.min(row, col) < 0 || row == Row || col == Col || grid[row][col] == 1 || visited[row][col] == 1){
            return 0;
        }
        if(row == Row - 1 && col == Col - 1){
            return 1;
        }
        visited[row][col] = 1;
        int count = 0; 
        count += dfs(grid, row + 1, col, visited);
        count += dfs(grid, row - 1, col, visited);
        count += dfs(grid, row, col + 1, visited);
        count += dfs(grid, row, col - 1, visited);
        visited[row][col] = 0;
        return count;
    }
}
