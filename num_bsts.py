class Solution:
    def numTrees(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1:
            return 1
        n_trees = [0 for i in range(n)]
        n_trees[0] = 1
        def sub_trees(k):
            if k < 1:
                return 1
            if n_trees[k - 1] > 0:
                return n_trees[k - 1]
            else:
                tot = 0
                for i in range(1, k + 1):
                    tot += sub_trees(i - 1) * sub_trees(k - i)
                n_trees[k - 1] = tot
                return tot
        return sub_trees(n)

if __name__ == "__main__":
    sol = Solution()
    print(sol.numTrees(3))