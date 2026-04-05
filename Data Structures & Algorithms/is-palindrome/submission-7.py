class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = re.sub(r'[^a-z0-9]', '', s, flags=re.IGNORECASE).lower()
        l, r = 0, len(newS) -1
        while l < r:
            if newS[l] != newS[r]:
                return False
            l = l + 1
            r = r - 1
        return True
            