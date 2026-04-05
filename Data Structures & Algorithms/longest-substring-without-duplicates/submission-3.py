class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        count = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            #only take the length of the sub string -> VERY IMPORTANT
            lenOfSubString = r - l + 1
            count = max(count, lenOfSubString)
        return count
        