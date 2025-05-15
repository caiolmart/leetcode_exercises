from typing import List


class Solution:
    def _build_graph(self, wordList):
        graph = {}
        for idx, word in enumerate(wordList[:-1]):
            if word not in graph:
                graph[word] = set()
            for other_word in wordList[idx + 1 :]:
                diffs = 0
                for c_word, c_other in zip(word, other_word):
                    if c_word != c_other:
                        diffs += 1
                        if diffs > 1:
                            break
                if diffs == 1:
                    graph[word].add(other_word)
                    if other_word not in graph:
                        graph[other_word] = set()
                    graph[other_word].add(word)
        return graph

    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        graph = self._build_graph([beginWord] + wordList)
        if endWord not in graph:
            return 0
        distances = {beginWord: 1}
        # previous = {beginWord: ''}
        queue = [beginWord]
        while queue:
            current_node = queue.pop(0)
            neighbors = graph[current_node]
            if endWord in neighbors:
                # previous[endWord] = current_node
                distances[endWord] = distances[current_node] + 1
                return distances[current_node] + 1 #, previous, distances
            for next_candidate in neighbors:
                if next_candidate not in distances:
                    # previous[next_candidate] = current_node
                    distances[next_candidate] = distances[current_node] + 1
                    queue.append(next_candidate)
        return 0


"""
We want the shortest path in a graph where each word is a node and each link
represents words with only one different character.

Solution:
    Build the graph:
        for every word in [beginWord] + wordList assign their links
        in a adjecency set

    BFS from beginWord to endWord
    return the length
"""

sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(sol._build_graph([beginWord] + wordList))
print(sol.ladderLength(beginWord, endWord, wordList))
# l, previous, distances = sol.ladderLength(beginWord, endWord, wordList)
# print(l)
# print('previous', previous)
# print('distances', distances)

# sol = Solution()
# beginWord = "hit"
# endWord = "hog"
# wordList = ["hot", "hog"]
# # print(sol._build_graph([beginWord] + wordList))
# l, previous, distances = sol.ladderLength(beginWord, endWord, wordList)
# print(l)
# print('previous', previous)
# print('distances', distances)
