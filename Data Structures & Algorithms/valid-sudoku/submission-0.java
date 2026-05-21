class Solution {
    public boolean isValidSudoku(char[][] board) {
        int rows = 9;
        int cols = 9; 
        for(int i = 0; i < rows; i++){
            Set<Character> set1 = new HashSet<>();
            for(int j = 0; j < cols; j++){
                if(set1.contains(board[i][j]) && board[i][j] != '.'){
                    return false;
                }
                else{
                    set1.add(board[i][j]);
                }
            }
        }
        for(int j = 0; j < cols; j++){
            Set<Character> set2 = new HashSet<>();
            for(int i = 0; i < rows; i++){
                if(set2.contains(board[i][j]) && board[i][j] != '.'){
                    return false;
                }
                else{ 
                    set2.add(board[i][j]);
                }
            }
        }
        for(int boxRow = 0; boxRow < 3; boxRow++){
            for(int boxCol = 0; boxCol < 3; boxCol++){
                Set<Character> set3 = new HashSet<>();
                for(int startRow = boxRow * 3; startRow < boxRow * 3 + 3; startRow++){
                    for(int startCol = boxCol * 3; startCol < boxCol * 3 + 3; startCol++){
                        if(set3.contains(board[startRow][startCol]) && board[startRow][startCol] != '.'){
                            return false;
                        }
                        else{ 
                            set3.add(board[startRow][startCol]);
                        }
                    }
                }
            }
        }
        return true;
    }
}
