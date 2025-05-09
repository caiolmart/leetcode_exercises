from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjencency_list = {}
        N = len(isConnected)
        for i in range(N):
            adjencency_list[i] = []
            for j in range(N):
                if isConnected[i][j] and i != j:
                    adjencency_list[i].append(j)

        unseen_nodes = set(adjencency_list.keys())
        n_provinces = 0
        while unseen_nodes:
            n_provinces += 1
            visited_nodes = set()
            head_node = unseen_nodes.pop()
            queue = set()
            queue.update(adjencency_list[head_node])
            visited_nodes.add(head_node)
            while queue:
                this_node = queue.pop()
                unseen_nodes.remove(this_node)
                visited_nodes.add(this_node)
                queue.update(adjencency_list[this_node])
                queue = queue.difference(visited_nodes)
        return n_provinces
