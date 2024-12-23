def knapsack_problem(weights, values, n, capacity):
    # dp[i][w] 表示前 i 個物品，背包容量為 w 時的最大價值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]  # dp[n+1][capacity+1] 的大小

    # 填充 dp 表格
    for i in range(1, n + 1):  # 遍歷物品
        for w in range(capacity + 1):  # 遍歷背包容量
            if weights[i - 1] <= w:
                # 如果當前物品的重量小於等於背包容量，則有兩種選擇：
                # 1. 不放入當前物品，背包容量不變，最大價值為 dp[i-1, w]
                # 2. 放入當前物品，則最大價值為 dp[i-1, w-weights[i-1]] + values[i-1]
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # 如果當前物品的重量大於背包容量，則不能放入此物品
                dp[i][w] = dp[i - 1][w]

    # 最後返回 dp[n][capacity]，即所有物品和背包容量 C 下的最大價值
    return dp[n][capacity]


def main():
    # 物品的重量
    weights = [2, 3, 4, 5]

    # 物品的價值
    values = [3, 4, 5, 6]

    # 物品的數量
    n = len(weights)  # 這裡有 4 個物品

    # 背包的容量
    capacity = 5  # 背包容量為 5

    # 計算最大價值
    max_value = knapsack_problem(weights, values, n, capacity)

    # 輸出結果
    print("The maximum value that can be carried in the knapsack is:", max_value)


# 執行主函數
if __name__ == "__main__":
    main()
