class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}  # maps character -> last seen index
        i = 0            # left pointer (start of window)
        max_len = 0

        for j in range(len(s)):
            char = s[j]

        

        # Check for a real conflict: char seen before AND still inside current window
            if char in char_index and char_index[char] >= i:
                i = char_index[char] + 1
            

        # Always update the character's latest position
            char_index[char] = j

        # Update max length using current window size
            max_len = max(max_len, j - i + 1)

        return max_len

        
       