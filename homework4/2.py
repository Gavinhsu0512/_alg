import numpy as np

# 定義積分的被積分函數
def integrand(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

# 蒙地卡羅積分
def monte_carlo_integration(num_samples=100000):
    # 隨機生成樣本
    x_samples = np.random.uniform(0, 1, num_samples)
    y_samples = np.random.uniform(0, 1, num_samples)
    z_samples = np.random.uniform(0, 1, num_samples)
    
    # 計算函數值的平均值
    values = integrand(x_samples, y_samples, z_samples)
    
    # 估計積分值
    integral_estimate = np.mean(values)
    return integral_estimate

# 計算積分
result = monte_carlo_integration()
print(f"蒙地卡羅積分結果：{result}")
