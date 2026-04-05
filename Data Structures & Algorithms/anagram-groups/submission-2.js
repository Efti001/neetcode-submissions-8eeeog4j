class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let map = {}

        //sort the string -> each words
        for (let i = 0; i < strs.length; i++)
        {
            let word = strs[i] //take each words
            let sortWord = word.split("").sort().join("")

            if (!map[sortWord])
            {
                map[sortWord] = [] //add sortWord to map with an array
                //map visual
                //map["aet"] = []
            }

            map[sortWord].push(word)
            //map visual
            //map["aet"] -> checks if exist -> yes
            //map["aet"] -> push word ("eat, ate, tea")
        }

        return Object.values(map)
        
    }
}
