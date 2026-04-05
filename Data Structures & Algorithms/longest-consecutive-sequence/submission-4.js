class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if (nums.length === 0) return 0;

        let set = new Set(nums);
        let arr = Array.from(set).sort((a, b) => a - b);

        let curr = 1;
        let longest = 1;

        for (let i = 1; i < arr.length; i++) {
            if (arr[i] === arr[i - 1] + 1) {
                curr++; // extend streak
            } else {
                curr = 1; // reset streak
            }

            longest = Math.max(longest, curr); // track max
        }

        return longest;
    }
}
