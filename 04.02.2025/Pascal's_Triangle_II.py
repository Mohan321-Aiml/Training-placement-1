class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n = rowIndex
        C = [1] * (n + 1)
        for k in range(1, (n//2) + 1):
            C[k] = C[k - 1]
            C[k] *= n - k + 1
            C[k] //= k
            C[n-k] = C[k]
        return C
