# 示例：檢查簡單的 P 和 NP 類問題

# P 問題: 排序一個數字列表（這是一個多項式時間算法）
def p_problem(arr):
    return sorted(arr)

# NP 問題: 子集和問題（給定一組數字，檢查是否能找到一個子集使其和等於目標）
def np_problem(arr, target):
    def subset_sum(arr, target, n):
        if target == 0:
            return True
        if n == 0:
            return False
        # 包含 arr[n-1] 或不包含 arr[n-1]
        return subset_sum(arr, target - arr[n-1], n-1) or subset_sum(arr, target, n-1)
    
    return subset_sum(arr, target, len(arr))

# NP-Complete 問題：3-SAT 問題（這裡我們用簡化的方式來示範）
def np_complete_problem(formula):
    # 這個方法不是真的3-SAT的解決方法，而是僅用來展示問題
    # 在現實中，3-SAT是非常困難的問題
    if formula == 'a OR b OR c':
        return True  # 假設公式總是成立
    return False

# 測試
if __name__ == "__main__":
    # 測試 P 問題
    arr = [5, 2, 8, 1, 3]
    sorted_arr = p_problem(arr)
    print(f"Sorted Array: {sorted_arr}")

    # 測試 NP 問題
    arr = [1, 2, 3, 9]
    target = 12
    print(f"Subset Sum Problem: {np_problem(arr, target)}")

    # 測試 NP-Complete 問題
    formula = 'a OR b OR c'
    print(f"3-SAT Problem: {np_complete_problem(formula)}")
