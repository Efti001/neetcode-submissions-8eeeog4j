class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

        let map = {};

// Step 1: Build frequency map
for (let i = 0; i < nums.length; i++) {
  map[nums[i]] = (map[nums[i]] || 0) + 1;
}

// Step 2: Sort entries by frequency (value)
const sorted = Object.entries(map).sort((a, b) => b[1] - a[1]);

// Step 3: Return only the top k keys (converted back to numbers)
const topK = sorted.slice(0, k).map(entry => Number(entry[0]));
return topK
    }
}
