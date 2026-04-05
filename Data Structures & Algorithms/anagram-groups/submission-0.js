class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let map = {} //hashmap to store all the words and find same valued pairs
        for (let i = 0; i < strs.length; i++)
        {
            let word = strs[i] //take current word
            let sortString = word.split("").sort().join("")
            if(!map[sortString]){
                map[sortString] = []
            }

            map[sortString].push(word)
        }

        return Object.values(map)
    }
}
