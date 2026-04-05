class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if len of both string doesn't match -> no anagram -> false
        if len(s) != len(t):
            return False
        #sort the string
        sortS = sorted(s)
        sortT= sorted(t)
        #see if both string matches -> true
        if sortS == sortT:
            return True
        else:
            return False