"""
Given an integer array, adjust each integers so that the difference of every adjacent integers are not greater than a given number target. If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of |A[i]-B[i]|
Example
Given [1,4,2,3] and target = 1, one of the solutions is [2,3,2,3], the adjustment cost is 2 and it's minimal. Return 2.

Solution :

定义res[i][j] 表示前 i个number with 最后一个number是j，这样的minimum adjusting cost

如果第i-1个数是j, 那么第i-2个数只能在[lowerRange, UpperRange]之间，lowerRange=Math.max(0, j-target), upperRange=Math.min(99, j+target),

这样的话，transfer function可以写成：

for (int p=lowerRange; p<= upperRange; p++) {

dp[i][j] = Math.min(res[i][j], dp[i-1][p] + Math.abs(j-A.get(i-1)));

}
"""

"""
Lintcode hard
"""
