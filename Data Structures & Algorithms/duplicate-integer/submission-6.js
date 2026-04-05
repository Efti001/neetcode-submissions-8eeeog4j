class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        //num is an array

        //iterate to go thru values
        //have 2 values -> i and j 
        //if i === j is the same return true

        for (let i = 0; i < nums.length; i++)
        {
            for (let j = i + 1; j < nums.length; j++ )
            {
                if (nums[i] === nums[j])
                {
                    return true
                }
            }
        }

        return false
    }
}
