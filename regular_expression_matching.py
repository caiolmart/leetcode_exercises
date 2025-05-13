class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_list = list(p)
        s_list = list(s)
        if len(s_list) == 0 and len(p_list) == 0:
            return True
        if len(p_list) == 0 and len(s_list) != 0:
            return False
        if len(s_list) == 0:
            while p_list:
                p_char = p_list.pop()
                if p_char != "*":
                    return False
                p_list.pop()
            return True

        p_char = p_list.pop()
        s_char = s_list.pop()
        if p_char == "*":
            p_char = p_list.pop()
            if s_char != p_char and p_char != '.':
                s_list.append(s_char)
                return self.isMatch("".join(s_list), "".join(p_list))

            # Ignore completely this * clause
            this_possibility = self.isMatch(
                s="".join(s_list + [s_char]), p="".join(p_list)
            )
            if this_possibility:
                return True
            while s_char == p_char or p_char == '.':
                this_possibility = self.isMatch(
                    s="".join(s_list), p="".join(p_list)
                )
                if this_possibility:
                    return True

                if s_list and (s_list[-1] == p_char or p_char == '.'):
                    s_char = s_list.pop()
                else:
                    return False

        elif p_char == "." or s_char == p_char:
            return self.isMatch(s="".join(s_list), p="".join(p_list))

        return False


sol = Solution()
print(sol.isMatch("aa", "a"))  # False
print(sol.isMatch("aa", "a*"))  # True
print(sol.isMatch("mississippi", "mis*is*ip*."))  # True
print(sol.isMatch("aab", "c*a*b"))  # True
print(sol.isMatch("aaa", "ab*a"))  # False
print(sol.isMatch("aaa", "ab*a*c*a"))  # True
print(sol.isMatch("aab", "b.*")) # False
print(sol.isMatch("ab", ".*")) # True
