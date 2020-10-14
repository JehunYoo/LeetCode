class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findPalindrome(left: int, right: int) -> str:
            while 0 <= left and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        palindrome = ''
        
        for i in range(len(s) - 1):
            palindrome = max(palindrome, findPalindrome(i, i + 2), findPalindrome(i, i + 3), key=len)
        
        return palindrome