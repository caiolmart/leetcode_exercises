from typing import List

class Solution:
    def is_valid(self, s: str) -> bool:
        aux = 0
        for i in range(len(s)):
            if s[i] == '(':
                aux += 1
            elif s[i] == ')':
                aux -= 1
                if aux < 0:
                    return False
        if aux == 0:
            return True
        return False
    
    def permutations(self, positions: List[int], n: int) -> List[List[int]]:
        if n == 0:
            return list()
        if n == 1:
            return [[x] for x in positions]
        perm = list()
        for i in range(len(positions) - n + 1):
            perm += [[positions[i]] + x for x in 
                        self.permutations(positions[(i+1):], n - 1)]
        return perm

    def remove_elements(self, s: str, rem: List[int]) -> str:
        rem = sorted(rem, reverse=True)
        rs = s
        for r in rem:
            rs = rs[:r] + rs[(r + 1):]
        return rs
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if self.is_valid(s):
            return [s]
        left = 0
        right = 0
        left_pos = list()
        right_pos = list()
        for i in range(len(s)):
            if s[i] == '(':
                left_pos.append(i)
                left += 1
            elif s[i] == ')':
                right_pos.append(i)
                if left > 0:
                    left -= 1
                else:
                    right += 1
        candidates = set()
        perm_left = self.permutations(left_pos, left)
        perm_right = self.permutations(right_pos, right)
        if len(perm_left) > 0 and len(perm_right) > 0:
            for rem_left in perm_left:
                for rem_right in perm_right:
                    rem = rem_left + rem_right
                    rem_str = self.remove_elements(s, rem)
                    if self.is_valid(rem_str):
                        candidates.add(rem_str)
        elif len(perm_left) > 0:
            for rem_left in perm_left:
                rem_str = self.remove_elements(s, rem_left)
                if self.is_valid(rem_str):
                    candidates.add(rem_str)
        elif len(perm_right) > 0:
            for rem_right in perm_right:
                rem_str = self.remove_elements(s, rem_right)
                if self.is_valid(rem_str):
                    candidates.add(rem_str)
        return list(candidates)
