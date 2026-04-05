class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const sortS = s.split('').sort().join('');
        const sortT = t.split('').sort().join('');



    if (sortS === sortT){
    return true;
}

return false;
    }
}
