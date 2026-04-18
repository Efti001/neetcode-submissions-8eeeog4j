class Solution:
    def isPalindrome(self, s: str) -> bool:
        regString = re.findall('[a-zA-Z0-9]', s.lower())
        l, r = 0, len(regString) - 1
        while l < r:
            if regString[l] == regString[r]:
                l += 1
                r -= 1
            else:
                return False
        return True