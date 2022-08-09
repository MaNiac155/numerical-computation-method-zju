# from sympy import *
# x = Symbol('x')
# fx = (-x ** 5 + 2 * 600 ** 2 * x ** 3 - 600 ** 4 * x) * 2.5 / (120 * 50000 * 30000 * 600)
# gx = fx.diff(x)
from math import *


def f(x):
    return (-x ** 5 + 2 * 600 ** 2 * x ** 3 - 600 ** 4 * x) * 2.5 / (120 * 50000 * 30000 * 600)


def g(x): #fx的导函数
    return -1.15740740740741e-13 * x ** 4 + 5.0e-8 * x ** 2 - 0.003


def gd(x):#gx的导函数
    return -4.62962962962964e-13 * x ** 3 + 1.0e-7 * x


def h(x): #不动点迭代用的函数
    return sqrt((0.003 + 1.15740740740741e-13 * x ** 4) / 5.0e-8)


# 二分法解方程
left = 0
right = 600
mid = (left + right) / 2
k = 0
eps_a = 1
while eps_a > 0.00001:

    if (right - left) > 0.00001 and g(mid) > 0:
        right = mid
    elif (right - left) > 0.00001 and g(mid) < 0:
        left = mid
    mid_n = (left + right) / 2
    k += 1
    eps_a = abs((mid_n - mid) / mid_n)
    mid = mid_n

k += 1
result = mid
print("二分法求得根为%d" % result)
print("二分次数为%d" % k)
print("挠度值为%.1f" % abs(f(result)))

# 试位法解方程

left = 0
right = 500
xr = right - g(right) * (left - right) / (g(left) - g(right))
k = 0
eps_a = 1

while eps_a > 0.00001:
    left = xr
    xr_n = right - g(right) * (left - right) / (g(left) - g(right))
    k += 1
    eps_a = abs((xr_n - xr) / xr_n)
    xr = xr_n
k += 1
result = xr
print("试位法求得根为%d" % result)
print("试位次数为%d" % k)
print("挠度值为%.1f" % abs(f(result)))

# 不动点迭代法

x0 = 1  # 初始值x0=1
eps_a = 1  # 近似误差
k = 0  # 迭代次数

while eps_a > 0.00001:
    x_new = h(x0)
    eps_a = abs((x_new - x0) / x_new)
    x0 = x_new
    k += 1

k += 1
result = x0
print("不动点迭代法求得根为%d" % result)
print("迭代次数为%d" % k)
print("挠度值为%.1f" % abs(f(result)))

# Newton-Raphson法

x0 = 80  # 初始值x0=80
# 注：此处x0太小的话，会直接跳过268这个根，到600。因此根据实际根的取值把x0初始值设大一点。
eps_a = 1  # 近似误差
k = 0  # 迭代次数

while True:
    while eps_a > 0.00001:
        x_new = x0 - g(x0) / gd(x0)
        eps_a = abs((x_new - x0) / x_new)
        x0 = x_new
        k += 1
    if abs(g(x0)) < 0.00000001:
        break

k += 1
result = x0
print("Newton-Raphson法求得根为%d" % result)
print("迭代次数为%d" % k)
print("挠度值为%.1f" % abs(f(result)))

# 割线法

x0 = 81  # 初始值x0=81
x01 = 80
# 和上一方法类似的情况
eps_a = 1  # 近似误差
k = 0  # 迭代次数

while eps_a > 0.00001:
    x_new = x0 - g(x0) * (x0 - x01) / (g(x0) - g(x01))
    eps_a = abs((x_new - x0) / x_new)
    x01 = x0
    x0 = x_new
    k += 1

k += 1
result = x0
print("割线法求得根为%d" % result)
print("迭代次数为%d" % k)
print("挠度值为%.1f" % abs(f(result)))
