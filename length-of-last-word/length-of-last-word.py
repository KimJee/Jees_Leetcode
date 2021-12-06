class Solution(object):
    def lengthOfLastWord(self, s):
        tokens = s.split()
        return len(tokens[-1])
        """
        :type s: str
        :rtype: int
        """
        