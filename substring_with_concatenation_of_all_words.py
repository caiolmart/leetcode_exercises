from typing import List

class Solution:
    def _count_words(self, s, l):
        counts = {}
        for idx in range(0, len(s), l):
            substr = s[idx:idx + l]
            if substr not in counts:
                counts[substr] = 1
            else:
                counts[substr] += 1
        return counts

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_dict = {}
        for word in words:
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1

        word_len = len(words[0])
        concat_len = word_len * len(words)

        ans = []
        if len(s) < concat_len:
            return ans
        
        for idx in range(len(s) - concat_len + 1):
            candidate_substring = s[idx: idx+concat_len]
            candidate_words = self._count_words(candidate_substring, word_len)
            if candidate_words == words_dict:
                ans.append(idx)

        return ans

"""
Store words in a set `words_set` for fast lookup
find the length of the words `word_len`
Concateneted string lenght is `concat_len = word_len * len(words_set)`
if len(s) < concat_len: return []

for each initial index (up to len(s) - concat_len) break the candidate substring
in a set of words:
candidate_substring = s[idx:idx + concat_len]
candidate_words = set(split(candidate_substring, word_len))
Check if the set is equal to the `word_set`

"""

sol = Solution()
# print(sol._split('abcd', 3))
print(sol.findSubstring('xabcdab', ['ab', 'cd']))
print(sol.findSubstring('xabcdab', ['ab', 'cd']))