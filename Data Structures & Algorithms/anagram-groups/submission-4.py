class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for i in range(len(strs)):
            word = strs[i] #take current word
            sortWord = "".join(sorted(word))
            if sortWord not in hashMap:
                hashMap[sortWord] = []
            hashMap[sortWord].append(word)
        return list(hashMap.values())