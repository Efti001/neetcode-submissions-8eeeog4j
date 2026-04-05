class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sortS = sorted(s)
        sortT = sorted(t)

        if len(sortS) != len(sortT):
            return False

        return sortS == sortT