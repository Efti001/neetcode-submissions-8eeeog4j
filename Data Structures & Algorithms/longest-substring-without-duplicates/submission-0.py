class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0 
        count = 0
        for r in range(len(s)):
            #if there's a dup in set, remove the leftmost char
            while s[r] in seen: #if the right char already exist in set
                seen.remove(s[l]) #remove the left most char
                l += 1          #move the left pointer to the next char
            seen.add(s[r]) #if new char, add to set
            count = max(count, r - l + 1)
        return count