import multiprocessing

def halt(f, input):
    def target(queue):
        try:
            f(input)
            queue.put(True)
        except:
            queue.put(False)

    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=target, args=(queue,))
    process.start()
    process.join(timeout=2)  # 設置最大執行時間為2秒

    if process.is_alive():
        process.terminate()
        return False  # 未在時間內完成，可能不會停機
    else:
        return queue.get()

def f1(n):
    return n * n

def f2(n):
    s = 0
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                for _ in range(n):
                    s = s + 1

print('halt(f1, 3) =', halt(f1, 3))   # 輸出: True
print('halt(f2, 10) =', halt(f2, 10)) # 輸出: True
print('halt(f2, 1000) =', halt(f2, 1000)) # 輸出: False
