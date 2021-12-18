#https://leetcode.com/problems/search-a-2d-matrix-ii/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[0] <= target <= i[-1]:
                if target in i:
                    return True
        return False


sl = Solution()
target = 9
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
print(sl.searchMatrix(matrix, target))
