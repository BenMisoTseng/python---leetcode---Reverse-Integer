class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        absX = abs(x)
        while( absX != 0):
            ans = ans * 10 + absX % 10
            absX /= 10
            print ans, absX
            if -(2 ** 31) > ans * -1 or ans > 2 ** 31 -1:
                return 0
        if x > 0:
            return ans
        else:
            return ans * -1