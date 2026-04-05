class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArray = list(s)
        tArray = list(t)

        sArray.sort()
        tArray.sort()

        

        if sArray == tArray:
            return True
        return False