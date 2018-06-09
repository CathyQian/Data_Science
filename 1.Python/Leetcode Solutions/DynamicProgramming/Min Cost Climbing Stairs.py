"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

"""
"""
动态规划 mincost[i] = min(mincost[i-1], mincost[i-2]) + cost[i],注意所有cost都为非负，
所以每一步找最小即可；如果cost可以为负数，那么不能每一步找最小数
相关题目：climbing stairs.
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        cost.append(0)
        mincost = [0] * (n+1)
        mincost[0], mincost[1] = cost[0], cost[1]
        for i in range(2, n+1):
            mincost[i] = min(mincost[i-1], mincost[i-2]) + cost[i]
        return mincost[-1]
