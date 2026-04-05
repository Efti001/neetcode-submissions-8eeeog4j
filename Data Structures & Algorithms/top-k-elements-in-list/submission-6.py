class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sMap = {}
        for i in range(len(nums)):
            sMap[nums[i]] = sMap.get(nums[i], 0) + 1
        sortmap = sorted(sMap, key=sMap.get, reverse=True)
        getK = sortmap[:k]
        return getK