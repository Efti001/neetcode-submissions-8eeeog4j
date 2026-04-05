class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;

        //sort and see it matches
        let sortS = s.split('').sort().join()
        let sortT = t.split('').sort().join()

        for (let i = 0; i < s.length; i++)
        {
            if (sortS === sortT)
            {
                return true
            }
        }
        
        return false
    }

}
