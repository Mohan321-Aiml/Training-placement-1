class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        previous1 = 1
        previous2 = 2
        for i in range(3,n+1):
            current = previous1 + previous2
            previous1 = previous2
            previous2 = current
        return previous2
        
