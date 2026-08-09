class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n < 2 and m < 2:
            return 1

        matrix = [[1] for i in range(m)]
        matrix[-1] = [1] * n

        print(matrix)
        for r in range(m - 2, -1, -1):
            for c in range(1, n):
                new_matrix_val = matrix[r + 1][-c - 1] + matrix[r][-c]
                matrix[r].insert(0, new_matrix_val)
        
        return matrix[0][0]