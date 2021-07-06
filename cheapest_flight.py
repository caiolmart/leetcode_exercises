from typing import List
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        edges = collections.defaultdict(list)
        for f in flights:
            edges[f[0]].append((f[1], f[2]))
        stack = {(src, 0) : 0}
        discovered = set()
        while stack:
            min_key = min(stack, key=stack.get)
            price = stack.pop(min_key)
            if min_key[0] == dst:
                return price
            discovered.add(min_key)
            next_d = min_key[1] + 1
            for flight in edges[min_key[0]]:
                if (flight[0], next_d) not in discovered:
                    if next_d <= K or flight[0] == dst:
                        if (flight[0], next_d) in stack:
                            stack[(flight[0], next_d)] = min(flight[1] + price, stack[(flight[0], next_d)])
                        else:
                            stack[(flight[0], next_d)] = flight[1] + price
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.findCheapestPrice(
        3,
        [[0,1,100],[1,2,100],[0,2,500]],
        0,
        2,
        1
    ))
    print(sol.findCheapestPrice(
        3,
        [[0,1,100],[1,2,100],[0,2,500]],
        0,
        2,
        0
    ))
