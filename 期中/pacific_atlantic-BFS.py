from collections import deque  # 引入 deque 來實現 BFS

def pacificAtlantic(heights):
    if not heights:
        return []

    m, n = len(heights), len(heights[0])

    # 用來記錄每個格子是否能流向太平洋
    pacific_reach = [[False] * n for _ in range(m)]  
    # 用來記錄每個格子是否能流向大西洋
    atlantic_reach = [[False] * n for _ in range(m)]  

    # 定義BFS函數，從起始點開始遍歷，標註能夠流向指定海洋的格子
    def bfs(start_points, ocean_reach):
        # 使用隊列來實現BFS
        queue = deque(start_points)
        # 四個方向：上、下、左、右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            i, j = queue.popleft()  # 取出隊列中的一個元素
            if ocean_reach[i][j]:  # 如果該格子已經被訪問過，則跳過
                continue
            ocean_reach[i][j] = True  # 標註該格子能流向指定海洋
            # 檢查四個方向，並將符合條件的相鄰格子加入隊列
            for dx, dy in directions:
                x, y = i + dx, j + dy
                # 確保相鄰格子在矩陣範圍內，並且水流可以流向這個格子
                if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
                    queue.append((x, y))  # 把符合條件的格子加入隊列繼續遍歷

    # 從太平洋的邊界進行BFS
    pacific_start_points = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]  # 左邊界和上邊界
    bfs(pacific_start_points, pacific_reach)

    # 從大西洋的邊界進行BFS
    atlantic_start_points = [(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)]  # 右邊界和下邊界
    bfs(atlantic_start_points, atlantic_reach)

    # 收集能夠同時流向兩個海洋的格子
    result = []
    for i in range(m):
        for j in range(n):
            if pacific_reach[i][j] and atlantic_reach[i][j]:
                result.append([i, j])

    return result

# 測試例子
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
print(pacificAtlantic(heights))  # 預期輸出：[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
