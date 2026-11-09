class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Sliding window varibale size
        #Condition is of K replacements

        #So left and right start at 0, and 1. then if left =right then right +1 and if left not equal to right then count = +1 , if count > k then left by 1

        # we cna store two things the first known outlier and last known acceptable
        #and we can use target
        new_accept = -1   # last index seen that matched the current target
        left = 0
        count = 0         # replacements needed in current window
        maximum = 0       # best window length found so far
        outlier = -1      # first index that broke the run
        freq = {}         # char -> how many times it appears in window

        right = 0
        while right < len(s):
            # Grow the window: add s[right]
            freq[s[right]] = 1 + freq.get(s[right], 0)

            # Most frequent char in window, and how many replacements we'd need
            maxf = max(freq.values())
            count = (right - left + 1) - maxf

            # If too many replacements needed, shrink from the left
            # (count only ever decreases when we drop the char that had max freq)
            if count > k:
                freq[s[left]] -= 1
                left += 1

            # Update best whenever the current window is valid
            if (right - left + 1) - max(freq.values()) <= k:
                maximum = max(maximum, right - left + 1)

            # Track which char index acted as the outlier/accept point (your idea)
            if right > left and s[right] == s[left]:
                new_accept = right
            elif right > left and outlier == -1:
                outlier = right

            right += 1

        return maximum
