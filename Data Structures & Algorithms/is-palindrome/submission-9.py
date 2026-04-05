class Solution:
    def isPalindrome(self, s: str) -> bool:
        reg = re.findall("[a-zA-Z0-9]", s.lower())
        l,r = 0, len(reg) - 1
        while l < r:
            if reg[l] != reg[r]:
                return False
            l += 1
            r -= 1
        return True 
        