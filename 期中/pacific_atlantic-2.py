def pacificAtlantic(heights):
    if not heights:
        return []

    m, n = len(heights), len(heights[0])
    pacific_reach = [[False] * n for _ in range(m)]
    atlantic_reach = [[False] * n for _ in range(m)]

    # 定義DFS函數，從當前格子進行深度優先搜索
    def dfs(i, j, ocean_reach):
        if ocean_reach[i][j]:
            return
        ocean_reach[i][j] = True
        # 四個方向：上、下、左、右
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
                dfs(x, y, ocean_reach)

    # 從太平洋邊界進行DFS
    for i in range(m):
        dfs(i, 0, pacific_reach)  # 左邊界
    for j in range(n):
        dfs(0, j, pacific_reach)  # 上邊界

    # 從大西洋邊界進行DFS
    for i in range(m):
        dfs(i, n-1, atlantic_reach)  # 右邊界
    for j in range(n):
        dfs(m-1, j, atlantic_reach)  # 下邊界

    # 收集能夠同時流向兩個海洋的格子
    result = []
    for i in range(m):
        for j in range(n):
            if pacific_reach[i][j] and atlantic_reach[i][j]:
                result.append([i, j])

    return result

heights = [[1]]
print(pacificAtlantic(heights))

