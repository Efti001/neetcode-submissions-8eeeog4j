class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}

        for i in range(len(strs)):
            word = strs[i]
            sortWord = ''.join(sorted(word))
            if sortWord not in hMap:
                hMap[sortWord] = []
            hMap[sortWord].append(word)

        return list(hMap.values())