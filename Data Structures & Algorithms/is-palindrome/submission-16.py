class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = re.findall('[a-zA-Z0-9]', s.lower())
        l = 0
        r = len(newString) - 1
        while l <= r:
            if newString[l] == newString[r]:
                l += 1
                r -= 1
            else:
                return False
        return True