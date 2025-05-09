from typing import List


class Solution:
    def _check_and_add(self, pos, candidate_pos, grid, land_adj_list):
        if grid[candidate_pos[0]][candidate_pos[1]]:
            land_adj_list[pos].add(candidate_pos)

            if candidate_pos not in land_adj_list:
                land_adj_list[candidate_pos] = set()

            land_adj_list[candidate_pos].add(pos)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        land_adj_list = {}
        m = len(grid)
        n = len(grid[0])
        for i in range(len(grid)):
            for j, element in enumerate(grid[i]):
                if element:
                    pos = (i, j)
                    if pos not in land_adj_list:
                        land_adj_list[pos] = set()
                    if i < m - 1:
                        self._check_and_add(
                            pos, (i + 1, j), grid, land_adj_list
                        )
                    if j < n - 1:
                        self._check_and_add(
                            pos, (i, j + 1), grid, land_adj_list
                        )

        not_visited = set(land_adj_list.keys())

        n_enclaves = 0

        while not_visited:
            has_exit = False
            this_root = not_visited.pop()
            component_size = 1
            if this_root[0] in [0, m - 1] or this_root[1] in [0, n - 1]:
                has_exit = True
            queue = land_adj_list[this_root]
            while queue:
                node = queue.pop()
                component_size += 1
                not_visited.remove(node)
                if node[0] in [0, m - 1] or node[1] in [0, n - 1]:
                    has_exit = True
                queue.update(land_adj_list[node].intersection(not_visited))

            if not has_exit:
                n_enclaves += component_size

        return n_enclaves


grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
sol = Solution()
# print(sol.numEnclaves(grid))

grid = [
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
]

print(sol.numEnclaves(grid))
