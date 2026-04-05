class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in strs:
            sortS = "".join(sorted(i))
            if  sortS not in hashMap:
                hashMap[sortS] = []
            hashMap[sortS].append(i)
                
        return list(hashMap.values())
            
            