"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

"""
本题的巧妙之处在于stack里面存有min和list, list里面的每一个元素存有之前list的min信息和
当前元素信息 (list_current = current - min of previous list)
if list_current < 0: update min
else: keep min
当执行pop操作时, 假设 x 为pop出来的元素，则有：
if x < 0:
    self.min = self.min - x
if x > 0:  do nothing
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x


    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x


    def top(self):
        """
        :rtype: int
        """
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
