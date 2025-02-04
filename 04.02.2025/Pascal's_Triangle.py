class Solution(object):
    def generate(self, numRows):
        L = []
        for i in range(1,numRows + 1):
            l1 = [1 for j in range(i)]
            if i>=3:
               for j in range(1,len(l1)-1):
                l1[j] = l2[j] + l2[j-1] 
            l2 = l1
            L.append(l1)
        return L
