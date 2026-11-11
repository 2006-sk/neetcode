class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] means s[i:] can be segmented into words
        dp = [False] * (len(s) + 1)
        # Base case: empty suffix is valid
        dp[len(s)] = True
        
        # Work backwards from the end of string s
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # Check if word w matches s starting at index i
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                # Break early if valid path found from index i
                if dp[i]:
                    break
        
        # dp[0] tells if entire string s is valid
        return dp[0]