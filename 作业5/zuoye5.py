import numpy as np
import math

import matplotlib.pyplot as plt


def speed(t):  # 原函数
    u = 1800
    m0 = 160000
    q = 2500
    g = 9.8
    v = u * math.log(m0 / (m0 - q * t)) - g * t
    # v=1800*math.log(160000/(160000-2500*t))-9.8*t
    return v


def height():  # 直接返回精确值
    return 10879.619404897


# 梯形公式
def trapezoid(start, end):
    integral = (end - start) * (speed(start) + speed(end)) / 2
    eps = abs((integral - height()) / height())
    return integral, eps


# Simpson公式
def simpson(start, end):
    fs = speed(start)
    fm = speed((start + end) / 2)
    fe = speed(end)
    integral = ((end - start) / 6) * (fs + 4 * fm + fe)
    eps = abs((integral - height()) / height())
    return integral, eps


# simpson 3/8
def simpson375(start, end):
    length = end - start
    fs = speed(start)
    fm = speed(start + length / 3)
    fn = speed(start + length * 2 / 3)
    fe = speed(end)
    integral = (length / 8) * (fs + 3 * fm + 3 * fn + fe)
    eps = abs((integral - height()) / height())
    return integral, eps


# Romberg
t_T = np.zeros((4, 6), dtype=float)  # 存储最终结果


def trap(a, b, l):  # 算第一组梯形值
    length = b - a
    if l == 0:
        t_T[0, 0] = (length / 2) * (speed(a) + speed(b))
    else:
        con = 0
        for i in range(1, 2 ** (l - 1) + 1):
            con += speed(a + (2 * i - 1) * (b - a) / (2 ** l))
        t_0l = 0.5 * t_T[0, l - 1] + (length / (2 ** l)) * con
        t_T[0, l] = t_0l


def pulse(m, k):  # 算S，C，R
    t_T[m, k] = ((4 ** m * t_T[m - 1, k + 1] - t_T[m - 1, k])
                 / (4 ** m - 1))


def romberg(a, b, eps):
    for i in range(4):  # 先算前四行，判断是否能输出
        trap(a, b, i)
    for k in range(3):
        pulse(1, k)
    for k in range(2):
        pulse(2, k)
    pulse(3, 0)
    for m in range(1, 4):
        if abs(t_T[m, 0] - t_T[m - 1, 0]) < eps:
            return t_T[m, 0]
    k = 0  # 循环算后面的
    while k == 0 or abs(t_T[3, k] - t_T[3, k - 1]) >= eps:
        trap(a, b, k + 4)
        pulse(1, k + 3)
        pulse(2, k + 2)
        pulse(3, k + 1)
        k += 1
    return t_T[3, k]


def Gauss(a, b):  # 高斯三点求积公式
    GauThree = {0.7745966692: 0.555555556, 0: 0.8888888889}
    GauSum = 0.0
    for key, value in GauThree.items():
        GauSum += speed(((b - a) * key + a + b) / 2) * value
        if (key > 0):
            GauSum += speed(((a - b) * key + a + b) / 2) * value
    GauSum = GauSum * (b - a) / 2
    return GauSum


tixing = trapezoid(0, 30)
print("梯形公式计算结果为", tixing[0], "\t误差是", tixing[1])
simp = simpson(0, 30)
print("Simpson公式计算结果为", simp[0], "\t误差是", simp[1])

simp_3 = simpson375(0, 30)
print("Simpson 3/8法则结果为", simp_3[0], "\t误差是", simp_3[1])
ans = romberg(0, 30, 0.01)
wucha = abs((ans - height()) / height())
print("romberg方法结果为", ans, "误差是", wucha, "\nT值表:")
print(t_T.T)
ans_g = Gauss(0, 30)
wucha_g = abs((ans_g - height()) / height())
print("Gauss方法结果为", ans_g,"误差是", wucha_g)


# 第二题微分
def diffv(t):
    return 720000000000 * (1 - t / 64) / (160000 - 2500 * t) ** 2 - 9.8


def accelerate(t0, h):  # h是中心差商的步长
    fdx = (speed(t0 + h) - speed(t0 - h)) / (2 * h)
    return fdx


t = np.linspace(0, 30, 3001)
v = np.linspace(0, 30, 3001)
a = np.linspace(0, 30, 3001)
dv = np.linspace(0, 30, 3001)

for i in range(t.size):
    v[i] = speed(t[i])
    a[i] = accelerate(t[i], 1)
    dv[i] = diffv(t[i])
plt.figure(figsize=(5, 7))
plt.subplot(211)
plt.plot(t, v, label="$v$", color="red")
plt.xlabel("time")
plt.ylabel("speed")

plt.subplot(212)
plt.plot(t, a, label="$a$", color="red")
plt.plot(t, dv, 'b--', label="$div$")
plt.xlabel("time")
plt.ylabel("accel")
plt.legend()
plt.show()