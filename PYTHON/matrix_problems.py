"""
Given a square matrix mat[][], the task is to swap the elements of the major and minor diagonals.

Major Diagonal: 
- Elements that lie from the top-left corner to the bottom-right corner of the matrix (i.e., where row index equals column index).
Minor Diagonal: 
- Elements that lie from the top-right corner to the bottom-left corner (i.e., where the sum of row and column indices equals n - 1).

Examples:

Input: mat[][] = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]]
Output: [[2, 1, 0],
        [3, 4, 5],
        [8, 7, 6]]
Explanation: 
- Major Diagonal = [0, 4, 8], Minor Diagonal = [2, 4, 6]. We are required to swap the diagonal elements of same row, thus after doing so, major diagonal will become minor and vice-versa. 
"""
class Solution:
    def swapDiagonal(self, mat):
        """
        since it is a square matrix, number of rows = number of columns = n
        we will iterate through each row i from 0 to n-1
        """
        n = len(mat)
        for i in range(n):
            mat[i][i], mat[i][n - 1 - i] = mat[i][n - 1 - i], mat[i][i]
        return mat