class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}

        for i in range(len(nums)):
            if nums[i] not in hMap:
                hMap[nums[i]] = 1
            else:
                hMap[nums[i]] += 1
        sortmap = sorted(hMap, key=hMap.get, reverse=True)
        kNum = sortmap[:k]
        return kNum