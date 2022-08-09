import numpy as np
import matplotlib.pyplot as plt


# 插值
def l0(x, x0, x1, x2):
    return (x - x1) * (x - x2) / ((x0 - x1) * (x0 - x2))


def l1(x, x0, x1, x2):
    return (x - x0) * (x - x2) / ((x1 - x0) * (x1 - x2))


def l2(x, x0, x1, x2):
    return (x - x0) * (x - x1) / ((x2 - x0) * (x2 - x1))


def L(x, y0, y1, y2, x0, x1, x2):
    return y0 * l0(x, x0, x1, x2) + y1 * l1(x, x0, x1, x2) + y2 * l2(x, x0, x1, x2)


#             0  1  2  3  4  5  6  7  8    9  10  11  12  13  14
x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], dtype=float)
y = np.array([6.7, 8.2, 9.58, 9.5, 9.7, 10, 9.96, 9.99,
              10.49, 10.59, 10.6, 10.8, 10.6, 10.9, 10.76])
y_cha = np.array([0, ])
for i in range(1, 14):
    tempY = y[i - 1:i + 2]
    b = x[i]
    a = x[i - 1]
    c = x[i + 1]

    tempX = np.linspace(a, c, 100)
    y_cha_n = np.array([L(t, tempY[0], tempY[1], tempY[2], a, b, c) for t in tempX])
    y_cha = np.append(y_cha, y_cha_n)

y_cha = y_cha[1:]
x_t = np.linspace(2, 16, 1300)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ro', x_t, y_cha, 'b')
plt.title("插值", fontproperties="SimSun")
plt.show()

# # # # 拟合

X1 = np.reciprocal(x)
Y1 = np.reciprocal(y)
Y2 = np.log(y)


# 生成系数矩阵A
def get_A(X, Y):
    N = len(X)
    m = 2
    A = []
    # 计算每一个方程的系数
    for i in range(m):
        a = []
        # 计算当前方程中的每一个系数
        for j in range(m):
            a.append(sum(X ** (i + j)))
        A.append(a)
    A[0][0] = N

    return A


# 计算方程组的向量b
def get_b(X, Y):
    m = 2
    b = []
    for i in range(m):
        b.append(sum(X ** i * Y))
    return b


# 第一个公式
A = get_A(X1, Y1)
b = get_b(X1, Y1)

a0, a1 = np.linalg.solve(A, b)

_X = np.arange(2, 16, 0.1)
_Y = np.array([x / (a0 * x + a1) for x in _X])

# 算误差
yhat = np.array([i / (a0 * i + a1) for i in x])
delta=np.subtract(y,yhat)
delta_sq1=np.sum(np.square(delta))/len(delta)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ro', _X, _Y, 'b', )
plt.title("1/y = {} + {}/x".format(a0, a1))
plt.show()

# 第二个公式
A = get_A(X1, Y2)
b = get_b(X1, Y2)

a0, a1 = np.linalg.solve(A, b)

_X = np.arange(2, 16, 0.1)
_Y = np.array([np.exp(a0 + a1 / x) for x in _X])

# 算误差
yhat=np.array([np.exp(a0 + a1 / i) for i in x])
delta=np.subtract(y,yhat)
delta_sq2=np.sum(np.square(delta))/len(delta)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ro', _X, _Y, 'b', )
plt.title("y = {} * e^{}/x".format(a0, a1))
plt.show()
print("误差一:{}\n误差二:{}".format(delta_sq1,delta_sq2))