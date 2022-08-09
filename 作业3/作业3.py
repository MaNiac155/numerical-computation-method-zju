import numpy as np

a1 = np.array([[-3, 1, 1],
               [1, -4, 2],
               [1, 2, -4]])
b1 = np.array([-1, 0, 0])
a2 = np.array([[-3, 1, 1, 0, 0, 0, 0],
               [1, -4, 1, 1, 0, 0, 0],
               [1, 1, -4, 0, 1, 0, 0],
               [0, 1, 0, -4, 1, 1, 1],
               [0, 0, 1, 1, -4, 1, 1],
               [0, 0, 0, 1, 1, -4, 2],
               [0, 0, 0, 1, 1, 2, -4]])
b2 = np.array([-1, 0, 0, 0, 0, 0, 0])
a3 = np.array([[-3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, -4, 1, 1, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, -4, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, -4, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 1, 1, -4, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, -4, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, -4, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, -4, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 1, 1, -4, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, -4, 2],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, -4]])
b3 = np.array([-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
a4 = np.array([[-3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, -4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, -4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, -4, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, -4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, -4, 1, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, -4, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, -4, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 1, -4, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, -4, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, -4, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -4, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -4, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -4, 2],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, -4]])
b4 = np.array([-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
a5 = np.array([[-3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, -4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, -4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, -4, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, -4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, -4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, -4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, -4, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 1, -4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, -4, 1, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, -4, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -4, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -4, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -4, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, -4, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -4, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -4, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -4, 2],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, -4]])
b5 = np.array([-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def Gauss(A, B):  # 原始高斯消去法
    A = A.tolist()
    B = B.tolist()
    N = len(A)
    for i in range(1, N):
        for j in range(i, N):
            # 计算消元因子delta
            delta = A[j][i - 1] / A[i - 1][i - 1]
            # 从第i-1行开始消元
            for k in range(i - 1, N):
                # 对A进行消元
                A[j][k] = A[j][k] - A[i - 1][k] * delta
            # 对B进行消元
            B[j] = B[j] - B[i - 1] * delta
    # 进行回代，直接将方程的解保留在B中
    B[N - 1] = B[N - 1] / A[N - 1][N - 1]
    for i in range(N - 2, -1, -1):
        for j in range(N - 1, i, -1):
            B[i] = B[i] - A[i][j] * B[j]
        B[i] = B[i] / A[i][i]
    # 返回所有解的列表
    print("高斯消去法的解为：", np.array(B).round(3))


def change(a, b, k, n):
    ans = 0
    maxn = 0
    for i in range(k, n):
        if ans < np.fabs(a[i][k]):
            ans = a[i][k]
            maxn = i
    a[[k, maxn], :] = a[[maxn, k], :]
    b[k], b[maxn] = b[maxn], b[k]


def CrossMain(a, b):  # 列主元消去法
    count = 0
    m, n = a.shape
    if (m < n):
        print("有根")
    else:
        l = np.zeros((n, n))
        for i in range(n):
            if (a[i][i] == 0):
                print("no answer")

        for k in range(n - 1):
            change(a, b, k, n)
            for i in range(k + 1, n):
                l[i][k] = a[i][k] / a[k][k]
                count += 1
                for j in range(m):
                    a[i][j] = a[i][j] - l[i][k] * a[k][j]
                    count += 1
                b[i] = b[i] - l[i][k] * b[k]

        x = np.zeros(n)
        x[n - 1] = b[n - 1] / a[n - 1][n - 1]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                b[i] -= a[i][j] * x[j]

            x[i] = b[i] / a[i][i]
        print('列主元消去法的解为', x.round(3))


def G_S(a, b, x, g):  # G-S迭代法
    x = x.astype(float)
    m, n = a.shape
    tempx = 0
    times = 0
    if (m >= n):
        while True:
            for i in range(n):
                s1 = 0
                tempx = x.copy()
                for j in range(n):
                    if i != j:
                        s1 += x[j] * a[i][j]
                x[i] = (b[i] - s1) / a[i][i]
                times += 1
            gap = max(abs(x - tempx))

            if gap < g:
                break
    print("GS迭代法方程的解是 ", x.round(3))


g = 1e-4

print('n=1:')
Gauss(a1, b1)
G_S(a1, b1, np.array([0, 0, 0]), g)
CrossMain(a1, b1)

print('n=2:')

Gauss(a2, b2)
G_S(a2, b2, np.array([0, 0, 0, 0, 0, 0, 0]), g)
CrossMain(a2, b2)
print('n=3:')
Gauss(a3, b3)
G_S(a3, b3, np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), g)
CrossMain(a2, b2)
print('n=4:')
Gauss(a4, b4)
G_S(a4, b4, np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), g)
CrossMain(a4, b4)
print('n=5:')
Gauss(a5, b5)
G_S(a5, b5, np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), g)
CrossMain(a5, b5)
