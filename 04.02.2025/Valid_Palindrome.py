class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from string import punctuation

        s = ''.join([x for x in s if x not in punctuation and x!=' ']).upper()
        if s==s[::-1]:
            return True
        return False
        
