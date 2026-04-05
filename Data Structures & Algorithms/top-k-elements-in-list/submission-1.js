class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
    const map = {}
    for (let i = 0; i < nums.length; i++)
    {
        map[nums[i]] = (map[nums[i]] || 0) + 1
    }


    //we can make this one line 
    const toArray = Object.entries(map) //hashMap to array 
    const sortArray = toArray.sort((a,b)=> b[1] - a [1])
    const returnK = sortArray.slice(0,k).map(x =>Number(x[0]))

    return returnK
    }
}
