class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}
        #go thru loop
        for i in range(len(strs)):
            #take each word, split and join
            word = strs[i]
            sortWord = "".join(sorted(word))
            #if not in hash map, insert
            if sortWord not in hMap:   
            #insert into empty array
                hMap[sortWord] = []
            hMap[sortWord].append(word)
        return list (hMap.values())
        #if in map, insert into the existing array