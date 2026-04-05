class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        for (let i = 0; i < nums.length; i++){
            for (let j = 0; j < i; j++){
                if (nums[i] == nums[j]){
                    return true
                }
            }
        }
        return false;
    }
}
