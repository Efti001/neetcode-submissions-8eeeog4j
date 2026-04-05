class Solution {
  /**
   * @param {string} s
   * @return {boolean}
   */
  isPalindrome(s) {
    let newStr = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
    let lp = 0;
    let rp = newStr.length - 1;

    while (lp < rp) {
      if (newStr[lp] !== newStr[rp]) {
        return false;
      }
      lp++;
      rp--;
    }

    return true;
  }
}
