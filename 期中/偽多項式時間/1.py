import numpy as np

# 背包問題的動態規劃解法
def knapsack(weights, values, capacity):
    n = len(weights)  # 物品的數量
    # 初始化一個 (n+1) x (capacity+1) 的二維陣列，所有元素初始為0
    dp = np.zeros((n + 1, capacity + 1))
    
    # 填充dp陣列
    for i in range(1, n + 1):  # 遍歷每個物品
        for w in range(1, capacity + 1):  # 遍歷每個容量
            if weights[i - 1] <= w:
                # 如果當前物品可以放進背包，選擇放入背包或不放入
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # 如果當前物品無法放入背包，繼續保持不放
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]  # 返回最大價值

# 測試背包問題
weights = [2, 3, 4, 5]  # 物品的重量
values = [3, 4, 5, 6]   # 物品的價值
capacity = 5            # 背包的容量

max_value = knapsack(weights, values, capacity)
print(f"最大可獲得的價值是: {max_value}")
