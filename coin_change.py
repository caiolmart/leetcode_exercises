from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        if amount == 0:
            return 0
        all_possible = [-1 for i in range(amount + 1)]
        all_possible[0] = 0
        for val in range(1, amount + 1):
            for c in coins:
                if c <= val:
                    n_coins = all_possible[val - c]
                    if n_coins != -1 and (n_coins + 1 < all_possible[val] or
                                          all_possible[val] == -1):
                        all_possible[val] = n_coins + 1
        return all_possible[amount]

if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1,2,5], 11))
    print(sol.coinChange([186,419,83,408], 6249))
    print(sol.coinChange([1,2147483647], 2))
