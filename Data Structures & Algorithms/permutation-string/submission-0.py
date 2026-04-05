class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        s1Map = {}
        for i in range(len(s1)):
            s1Map[s1[i]] = s1Map.get(s1[i], 0) + 1 #map all the s1 char
        for i in range(n2 - n1 + 1):
            # to match the s1 len, we slice and make s2 same len as s1
            chunk = s2[i: i + n1]
            s2Map = {}
            for char in chunk:
                s2Map[char] = s2Map.get(char, 0) + 1
            if s2Map == s1Map:
                return True
        return False
