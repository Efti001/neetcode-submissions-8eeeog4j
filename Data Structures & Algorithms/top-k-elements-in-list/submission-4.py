from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Count the frequency of each number
        counts = Counter(nums)
        
        # 2. Get the 'k' most common elements
        # most_common returns a list of tuples: [(val1, count1), (val2, count2)]
        most_common_pairs = counts.most_common(k)
        
        # 3. Use a list comprehension to extract only the values (the first element of each tuple)
        return [val for val, count in most_common_pairs]