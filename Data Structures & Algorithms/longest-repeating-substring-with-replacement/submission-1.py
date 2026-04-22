class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        se = defaultdict(int)
        r, l = 0,0
        long = 0
        wind = 0
        max_f = 0
        for i in range(len(s)):
            r = i
            se[s[r]] += 1
            max_f = max(max_f, se[s[r]])

            wind = r - l + 1 
            num_len = wind - max_f
            while num_len > k:
                se[s[l]] -= 1
                l += 1
                wind = r - l + 1 
                # Recalculate max_f or use current logic; max_f doesn't strictly need 
                # to decrease for the window size logic to work correctly.
                max_f = max(se.values()) if se else 0
                num_len = wind - max_f
            long = max(long, r - l + 1)
        return long
        


