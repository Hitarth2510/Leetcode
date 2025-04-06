class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the input list.
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for the first element.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1  # Need a larger sum.
                elif total > 0:
                    right -= 1  # Need a smaller sum.
                else:
                    # Found a triplet that sums to 0.
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for left and right.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
        return res
