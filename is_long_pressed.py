class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while i < len(name) or j < len(typed):
            if j >= len(typed):
                return False
            if i >= len(name) or name[i] != typed[j]:
                if j == 0 or i == 0:
                    return False
                if typed[j] != typed[j - 1] or typed[j] != name[i - 1]:
                    return False
                j += 1
            else:
                j += 1
                i += 1
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isLongPressedName("alex", "aaleex"))
    print(sol.isLongPressedName("saeed", "ssaaedd"))
    print(sol.isLongPressedName("leelee", "lleeelee"))
    print(sol.isLongPressedName("laiden", "laiden"))
    print(sol.isLongPressedName("pyplrz", "ppyypllr"))