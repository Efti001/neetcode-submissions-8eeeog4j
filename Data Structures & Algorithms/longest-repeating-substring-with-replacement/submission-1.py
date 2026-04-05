class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        maxCount = 0 
        sMap = {}
        maxFreq = 0
        for r in range (len(s)):
            #store in sMap
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            #get most freq character 
            maxFreq = max(maxFreq, sMap[s[r]])

            #now use sliding window to shrink until k is met
            while (r - l + 1) -  maxFreq > k:
                sMap[s[l]] -= 1
                l += 1
            maxCount = max(maxCount, r - l + 1)
        return maxCount