class Solution(object):
    def searchMatrix(self, grid, r, c, t):
        low, high = 0, r * c - 1
        while low <= high:
            mid = low + (high - low) // 2
            row = mid // c
            col = mid % c
            val = grid[row][col]
            if val == t:
                return f"{row} {col}"
            elif val < t:
                low = mid + 1
            else:
                high = mid - 1
        return "-1 -1"

r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]
t = int(input())
print(Solution().searchMatrix(grid, r, c, t))
