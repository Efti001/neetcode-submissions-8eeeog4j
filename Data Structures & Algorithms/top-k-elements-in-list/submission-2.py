class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = 1 + hm.get(nums[i], 0)
        sortArr = sorted(hm.items(), key = lambda x:x[1], reverse = True)
        return [x[0] for x in sortArr[:k]]