class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #loop thru index i and j, see if it matches return true else false
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False