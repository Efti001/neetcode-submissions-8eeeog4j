class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sMap = {}

        for i in range(len(strs)):
            #separate each word
            word = strs[i]
            sortWord = ''.join(sorted(word))
            if sortWord not in sMap:
                sMap[sortWord] = []
            sMap[sortWord].append(word)
        return list(sMap.values())