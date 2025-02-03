class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j_start = 0
        count = 0
        for i in range(m + n):
            if i + 1 <= m + count:
                for j in range(j_start, n):
                    if nums1[i] < nums2[j]:
                        continue
                    else:
                        j_start = j + 1
                        count += 1
                        nums1.pop()
                        nums1.insert(i, nums2[j])
                        break
            else:
                for j in range(j_start, n):
                    nums1[j + m] = nums2[j]
                break
                
        return nums1 
                
        
