class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hashSet = new Set()

        for (let x = 0; x < nums.length; x++)
        {
            if (hashSet.has(nums[x])){
                return true
            }
            hashSet.add(nums[x])
        }
        return false
    }
}
