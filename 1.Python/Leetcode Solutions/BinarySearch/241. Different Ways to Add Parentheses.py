"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
"""
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        r = []
        for i, char in enumerate(input):
            if char in '+-*':
                part1 = self.diffWaysToCompute(input[:i])
                part2 = self.diffWaysToCompute(input[i+1:])
                for x in part1:
                    r += [eval(str(x) + char + str(y)) for y in part2]

        if r == []:
            r.append(input)

        return r
