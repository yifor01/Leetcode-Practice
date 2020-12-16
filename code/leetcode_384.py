# 384. Shuffle an Array (Medium)
'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
'''

# Solution by Yifor
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums
        
    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        return random.sample(self.original,len(self.original))

'''time complexity: O(n) , space complexity: O(n)'''
