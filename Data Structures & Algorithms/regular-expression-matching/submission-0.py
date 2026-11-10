class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Cache results for (i, j) states to avoid recomputation
        cache = {}

        def dfs(i: int, j: int) -> bool:
            # Return cached result if already computed
            if (i, j) in cache:
                return cache[(i, j)]
            
            # If pattern is exhausted, text must also be exhausted
            if j == len(p):
                return i == len(s)
            
            # Check if current characters match
            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # Handle star wildcard in pattern
            if (j + 1) < len(p) and p[j + 1] == '*':
                # Choice 1: Skip star (use 0 occurrences of preceding character)
                # Choice 2: Use star if character matches (advance text pointer)
                ans = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                # Normal character matching
                ans = first_match and dfs(i + 1, j + 1)
            
            # Store result in cache and return
            cache[(i, j)] = ans
            return ans

        return dfs(0, 0)