class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) return false

        let sortS = s.split("").sort().join("")
        let sortT = t.split("").sort().join("")

        if (sortS === sortT)
        {
            return true
        }

        return false
    }
}
