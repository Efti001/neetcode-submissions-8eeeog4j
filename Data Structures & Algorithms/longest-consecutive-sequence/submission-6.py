class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) #nums sorted and no dups
        longest = 0 #keep track of lcs

        for i in s:
            if i - 1 not in s: # i -> 1 -- if 0 not in set
                next_num = i + 1 #check to right 1 --> 2 (see if 2 exist)
                length = 1 #min len will be 1
                while next_num in s: #if 2 exist continue, if 3 exist continue etc
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest