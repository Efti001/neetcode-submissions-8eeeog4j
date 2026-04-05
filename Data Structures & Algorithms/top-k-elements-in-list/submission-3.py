class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kMap = {}
        for i in range(len(nums)):
            kMap[nums[i]] = 1 + kMap.get(nums[i], 0)
        sortMap = sorted(kMap.items(), key = lambda x:x[1], reverse = True)
        return [x[0] for x in sortMap[:k]]