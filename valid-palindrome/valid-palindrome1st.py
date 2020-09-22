import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = re.compile('[a-zA-Z0-9]')
        s = list(map(str.lower, p.findall(s)))
        mid = len(s) // 2
        end = len(s) - 1
        
        for idx, ch in enumerate(s[:mid]):
            if ch == s[end - idx]:
                pass
            else:
                return False
        else:
            return True

'''
Runtime: 84 ms, faster than 12.04% of Python3 online submissions for Valid Palindrome.
Memory Usage: 20.3 MB, less than 5.03% of Python3 online submissions for Valid Palindrome.
'''