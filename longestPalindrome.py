class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_palindrome_matrix = [
            [i == j for i in range(len(s))] for j in range(len(s))
        ]
        best_pos = (0, 0)
        has_any_odd = True

        # parallel diagonal
        has_any_even = False
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                is_palindrome_matrix[i][i + 1] = True
                best_pos = (i, i + 1)
                has_any_even = True

        for offset in range(2, len(s)):
            if offset % 2:
                if not has_any_even:
                    continue
                has_any_even = False
            else:
                if not has_any_odd:
                    continue
                has_any_odd = False
            for i in range(0, len(s) - offset):
                if (
                    is_palindrome_matrix[i + 1][i + offset - 1]
                    and s[i] == s[i + offset]
                ):
                    is_palindrome_matrix[i][i + offset] = True
                    best_pos = (i, i + offset)
                    if offset % 2:
                        has_any_even = True
                    else:
                        has_any_odd = True
            if not has_any_even and not has_any_odd:
                break

        return s[best_pos[0] : best_pos[1] + 1]


sol = Solution()
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("cbbca"))
print(sol.longestPalindrome("cbbbca"))
print(sol.longestPalindrome("ccd"))
print(sol.longestPalindrome("aacabdkacaa"))
