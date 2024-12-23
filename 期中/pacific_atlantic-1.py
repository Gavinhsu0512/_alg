def pacificAtlantic(heights):
    # 如果高度矩陣是空的，則返回空列表
    if not heights:
        return []

    # 獲取矩陣的行數 m 和列數 n
    m, n = len(heights), len(heights[0])

    # 初始化兩個矩陣，記錄哪些格子能夠到達太平洋（pacific_reach）和大西洋（atlantic_reach）
    pacific_reach = [[False] * n for _ in range(m)]  # 用來標註能夠到達太平洋的格子
    atlantic_reach = [[False] * n for _ in range(m)]  # 用來標註能夠到達大西洋的格子

    # 定義一個 DFS 函數，用來遍歷格子並標註能夠到達的海洋
    def dfs(i, j, ocean_reach):
        # 如果該格子已經被標註過，則返回
        if ocean_reach[i][j]:
            return
        # 標註該格子為可以流向指定海洋的格子
        ocean_reach[i][j] = True
        # 遍歷四個方向：上、下、左、右，並且檢查相鄰格子的高度是否小於等於當前格子的高度
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            # 確保相鄰格子在矩陣範圍內，並且相鄰格子的高度大於或等於當前格子
            if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
                # 遞歸調用 DFS，進行深度優先搜索
                dfs(x, y, ocean_reach)

    # 從太平洋的邊界進行 DFS 標註可以流向太平洋的格子
    for i in range(m):
        dfs(i, 0, pacific_reach)  # 左邊界（第一列）
    for j in range(n):
        dfs(0, j, pacific_reach)  # 上邊界（第一行）

    # 從大西洋的邊界進行 DFS 標註可以流向大西洋的格子
    for i in range(m):
        dfs(i, n-1, atlantic_reach)  # 右邊界（最後一列）
    for j in range(n):
        dfs(m-1, j, atlantic_reach)  # 下邊界（最後一行）

    # 收集能夠同時流向兩個海洋的格子
    result = []
    for i in range(m):
        for j in range(n):
            # 如果該格子同時能流向太平洋和大西洋，則加入結果列表
            if pacific_reach[i][j] and atlantic_reach[i][j]:
                result.append([i, j])

    return result  # 返回結果列表，包含所有能流向兩個海洋的格子

# 測試例子
heights = [
    [1, 2, 2, 3, 5],  # 第一行
    [3, 2, 3, 4, 4],  # 第二行
    [2, 4, 5, 3, 1],  # 第三行
    [6, 7, 1, 4, 5],  # 第四行
    [5, 1, 1, 2, 4]   # 第五行
]

# 呼叫函數並打印結果
print(pacificAtlantic(heights))  # 輸出結果：[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
