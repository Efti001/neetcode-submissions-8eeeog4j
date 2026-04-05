class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create hashmap
        hashMap = {}
        # sort the word
        for i in range(len(strs)):
            #take one word at a time
            word = strs[i]
            sortWord = ''.join(sorted(word))
            if sortWord not in hashMap:
                hashMap[sortWord] = []
            
            hashMap[sortWord].append(word)
        return list(hashMap.values())

        # insert word into hashmap
        # move to next word
        # see if word matches with current word in the hashmap
        # if yes, group
        # if not, add into hashmap