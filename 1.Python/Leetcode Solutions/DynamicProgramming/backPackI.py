"""
Given n items with size A[i], an integer m denotes the size of a backpack. How full you can fill this backpack?
"""

def backPack(self, m, A):
        # write your code here
        n = len(A)
        f = [0 for i in range(m+1)]
        for i in range(1, n+1):
            pre = list(f)
            for j in range(1, m+1):
                if j >= A[i-1]:
                    f[j] = max(pre[j], pre[j-A[i-1]] + A[i-1])
                else:
                    f[j] = pre[j]

        return f[m]
