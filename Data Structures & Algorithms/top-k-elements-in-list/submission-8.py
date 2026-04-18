class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        for i in range(len(nums)):
            hMap[nums[i]] = hMap.get(nums[i], 0) + 1
        sortedNums = sorted(hMap.keys(), key=hMap.get, reverse=True)
        res = (sortedNums[:k])
        return res