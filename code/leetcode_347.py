# 347. Top K Frequent Elements
'''
Question:
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

# Solution by Yifor
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]] += 1
        count = [x for x in dict1.values()]
        target = sorted(count)[len(dict1)-k]
        for i in nums:
            if (dict1.get(i)>= target) & (i not in ans)  & ( len(ans)<=k) :
                ans.append(i)
        return ans

'''time complexity: O(n logn) , space complexity: O(n)'''

# Best Solution (bucket sort)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = {}
        n = len(nums) 
        for i in range(n):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        buckets = [ [] for _ in range(n+1)]
        for i in count.keys():
            buckets[ count[i] ].append(i)
        for i in range(n,0,-1):
            ans+=buckets[i]
            if len(ans)==k:
                break
            
        return ans
        
'''time complexity: O(n) , space complexity: O(n)'''  