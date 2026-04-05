class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const set = new Set()
        const result = []
        for (let i = 0; i < nums.length; i++)
        {
            for (let j = i + 1; j < nums.length; j++)
            {
                for (let k = j + 1; k < nums.length; k++)
                {
                    if (nums[i] + nums[j] + nums[k] === 0)
                    {
                        const triplet = [nums[i], nums[j], nums[k]].sort((a, b) => a - b);
                        const toStr = triplet.toString()
                        set.add(toStr) 
                    }
                }
            }
        }

           for (const tripletStr of set) {
            result.push(tripletStr.split(',').map(Number));
        }

        return result;
    }
}
