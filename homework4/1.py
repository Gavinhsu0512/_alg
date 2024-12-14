import numpy as np
from scipy.integrate import tplquad

# 定義積分的被積分函數
def integrand(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

# 計算三重積分
result, error = tplquad(integrand, 0, 1,  # x 範圍
                        lambda x: 0, lambda x: 1,  # y 範圍
                        lambda x, y: 0, lambda x, y: 1)  # z 範圍

print(f"積分結果：{result}, 估算誤差：{error}")
