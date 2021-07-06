from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict or s == '':
            return True
        if not wordDict:
            return False
        max_len = max(len(x) for x in wordDict)
        
        def _sub_wordBreak(s, wordDict, max_len, begin, begin_list):
            if s[begin:] in wordDict or s == '':
                return True
            if begin_list[begin]:
                return False
            for i in range(begin + 1, begin + min(len(s) - begin, max_len + 1)):
                if s[begin:i] in wordDict and _sub_wordBreak(s, wordDict, max_len, i, begin_list):
                    return True
            begin_list[begin] = True
            return False
        begin_list = [False for i in range(len(s))]
        return _sub_wordBreak(s, wordDict, max_len, 0, begin_list)

if __name__ == "__main__":
    sol = Solution()
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(sol.wordBreak(s, wordDict))
