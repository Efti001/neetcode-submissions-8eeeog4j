class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let newStr = s.replace(/[^A-Za-z0-9]/g, "").toLowerCase()
        console.log(newStr)
        let left = 0;
        let right = newStr.length - 1;

        while (left < right)
        {

        if (newStr[left] === newStr[right])
        {
            left++
            right--
        }
        else{
            return false
        }
        }
        return true

        
    }
}
