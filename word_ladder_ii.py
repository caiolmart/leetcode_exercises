from typing import List, Set, Tuple


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
    
    def _get_paths(self, word, previous_dict) -> Set[Tuple[str]]:
        if not previous_dict[word]:
            return {(word,), }
        
        paths = set()
        previous_words = previous_dict[word]
        for this_word in previous_words:
            this_paths = self._get_paths(this_word, previous_dict)
            for path in this_paths:
                paths.add(tuple(list(path) + [word]))
        return paths

    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        graph = self._build_graph([beginWord] + wordList)
        if endWord not in graph:
            return []
        distances = {beginWord: 1}
        previous = {beginWord: []}
        queue = [beginWord]
        while queue:
            current_node = queue.pop(0)
            if current_node == endWord:
                break
            cur_dist = distances[current_node]
            neighbors = graph[current_node]
            for next_candidate in neighbors:
                if next_candidate not in distances:
                    previous[next_candidate] = [current_node]
                    distances[next_candidate] = distances[current_node] + 1
                    queue.append(next_candidate)
                elif cur_dist + 1 == distances[next_candidate]:
                    previous[next_candidate].append(current_node)
        
        if endWord not in previous:
            return []
        
        path_set = self._get_paths(endWord, previous)
        path_list = [
            list(tup_path) for tup_path in path_set
        ]
        return path_list


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
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# print(sol._build_graph([beginWord] + wordList))
# print(sol.findLadders(beginWord, endWord, wordList))
# l, previous, distances = sol.findLadders(beginWord, endWord, wordList)
# print(l)
# print('previous', previous)
# print('distances', distances)

# sol = Solution()
# beginWord = "hit"
# endWord = "hot"
# wordList = ["hot", "hog"]
# paths = sol.findLadders(beginWord, endWord, wordList)
# print(paths)
# previous, paths = sol.findLadders(beginWord, endWord, wordList)
# print(previous, paths)
# print(sol._build_graph([beginWord] + wordList))
# l, previous, distances = sol.findLadders(beginWord, endWord, wordList)
# print(l)
# print('previous', previous)
# print('distances', distances)

beginWord = "talk"
endWord = "tail"
wordList = ["talk","tons","fall","tail","gale","hall","negs"]
paths = sol.findLadders(beginWord, endWord, wordList)
print(paths)
