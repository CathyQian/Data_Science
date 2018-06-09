# backpack II

"""
Given n items with size A[i] and value V[i], and a backpack with size m
what is the maximum value you can put into the backpack?
"""
# similar to backPackI but replace A with V when calculating f
def backPack(m, A, V):
     n = len(A)
        f = [0 for i in range(m+1)]
        for i in range(1, n+1):
            pre = list(f)
            for j in range(1, m+1):
                if j >= A[i-1]:
                    f[j] = max(pre[j], pre[j-V[i-1]] + V[i-1])
                else:
                    f[j] = pre[j]

        return f[m]
