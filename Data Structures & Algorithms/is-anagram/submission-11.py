class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=  len(t):
            return False
        sortS = sorted(s)
        sortT = sorted(t)
        if sortS == sortT:
            return True
        return False