class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hMap = {}
        for i in range(len(strs)):
            word = strs[i]
            sortedWord = "".join(sorted(word))
            if sortedWord not in hMap:
                hMap[sortedWord] = []
            hMap[sortedWord].append(word)
        return list(hMap.values())
