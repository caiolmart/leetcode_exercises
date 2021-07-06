""" Testing ep1.py """

import pytest

from invalid_parentheses import Solution

############################################################
# Tests for part 1.

sol = Solution()

def test_is_valid():
    expected = [("()())()", False),
                ("(a)())()", False),
                (")(", False),
                ("()", True),
                ("(())()", True),
                ("(a)()()", True)]

    for e in expected:
        assert sol.is_valid(e[0]) == e[1]

def test_permutations():
    expected = [(([1, 2, 3], 0), []),
                (([1, 2, 3], 1), [[1], [2], [3]]),
                (([1, 2, 3], 2), [[1, 2], [1, 3], [2, 3]]),
                (([1, 2, 3], 3), [[1, 2, 3]])]

    for e in expected:
        assert sol.permutations(e[0][0], e[0][1]) == e[1]

def test_remove_elements():
    expected = [(('abcdef', [1]), ('acdef')),
                (('abcdef', [0, 1]), ('cdef')), 
                (('abcdef', [0, 4, 5]), ('bcd'))]
    for e in expected:
        assert sol.remove_elements(e[0][0], e[0][1]) == e[1]

def test_removeInvalidParentheses():
    expected = [('()', ['()']),
                ('()())()', ["()()()", "(())()"]),
                ("(a)())()", ["(a)()()", "(a())()"]),
                (")(", [""])]
    for e in expected:
        assert set(sol.removeInvalidParentheses(e[0])) == set(e[1])