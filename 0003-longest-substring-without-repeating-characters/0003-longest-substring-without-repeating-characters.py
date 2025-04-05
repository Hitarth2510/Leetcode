class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}      # Dictionary to store the last seen index of each character.
        start = 0      # Left pointer of the current window.
        max_length = 0 # Maximum length found so far.
        
        for i, char in enumerate(s):
            # If the character is already in the current window, move start pointer
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            seen[char] = i
            max_length = max(max_length, i - start + 1)
            
        return max_length