import numpy as np
import math
import time

start = time.perf_counter()

# 公式1

x = np.float32(1)  # 单精度，x代入1
y = np.float32(0)  # 当前近似值
y0 = y  # y0用来表示上一次计算的近似值
n = np.float32(1)  # 迭代次数
ln2_t = math.log(2)  # ln2的真值
epsilon_s = np.float32((0.5 * 10 ** (2 - 4)) * 0.01)  # 4位有效数字
# epsilon_s = np.float32((0.5 * 10 ** (2 - 6)) * 0.01)  # 6位有效数字
epsilon_a = np.float32(1)  # 初始值只要求它大于εs，使其进入循环即可。

while epsilon_a >= epsilon_s:  # 迭代方法限定有效数字4位
    item = np.float32((-1) ** (n + 1) * x ** n / n)  # 通项
    y += item
    epsilon_a = abs((y - y0) / y)  # 此处取绝对值
    y0 = y
    n += 1

print("ln2的真值是: ", ln2_t)
print("公式1: ")
print("单精度: y={}, n={}, epsilon_s={:.8f}, epsilon_a={:.10f}".format(y, n, epsilon_s, epsilon_a))

x = np.float64(1)  # 双精度
y = np.float64(0)
y1 = np.float64(0)
n = np.float64(1)
epsilon_s = np.float64((0.5 * 10 ** (2 - 4)) * 0.01)
# epsilon_s = np.float64((0.5 * 10 ** (2 - 6)) * 0.01)  # 6位有效数字
epsilon_a = np.float64(1)

while epsilon_a >= epsilon_s:
    item = np.float64((-1) ** (n + 1) * x ** n / n)
    y += item
    epsilon_a = abs((y - y1) / y)
    y1 = y
    n += 1
print("双精度: y={}, n={}, epsilon_s={:.8f}, epsilon_a={:.10f}".format(y, n, epsilon_s, epsilon_a))

# 公式2

x = np.float32(1 / 3)
y = np.float32(0)
y0 = y
n = np.float32(0)
epsilon_s = np.float32((0.5 * 10 ** (2 - 4)) * 0.01)
#epsilon_s = np.float32((0.5 * 10 ** (2 - 6)) * 0.01)  # 6位有效数字
epsilon_a = np.float32(1)  # 初始值只要求它大于εs，使其进入循环即可。

while epsilon_a >= epsilon_s:
    item = np.float32(2 * x ** (2 * n + 1) / (2 * n + 1))
    y += item
    epsilon_a = abs((y - y0) / y)
    y0 = y
    n += 1

print("公式2: ")
print("单精度: y={}, n={}, epsilon_s={:.8f}, epsilon_a={:.10f}".format(y, n, epsilon_s, epsilon_a))

x = np.float64(1 / 3)
y = np.float64(0)
y1 = np.float64(0)
n = np.float64(0)
epsilon_s = np.float64((0.5 * 10 ** (2 - 4)) * 0.01)
#epsilon_s = np.float64((0.5 * 10 ** (2 - 6)) * 0.01)  # 6位有效数字
epsilon_a = np.float64(1)

while epsilon_a >= epsilon_s:
    item = np.float64(2 * x ** (2 * n + 1) / (2 * n + 1))
    y += item
    epsilon_a = abs((y - y1) / y)
    y1 = y
    n += 1
print("双精度: y={}, n={}, epsilon_s={:.8f}, epsilon_a={:.10f}".format(y, n, epsilon_s, epsilon_a))

end = time.perf_counter()
print("运行耗时", end-start)
