class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let newStr = s.replace(/[^a-z0-9]/gi, "").toLowerCase();
        let left = 0;
        let right = newStr.length - 1

        console.log(newStr)
        while (left < right)
        {
            if (newStr[left] !== newStr[right])
            {
                return false
            }
            
            left++
            right--
        }
    return true
    }
}
