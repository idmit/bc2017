import sys
from collections import defaultdict

available = set(map(int, sys.stdin.readline().split()))

rules = defaultdict(list)

for line in sys.stdin:
    lhs_str, rhs_str = line.split('->')

    lhs = frozenset(map(int, lhs_str.split('+')))
    rhs = frozenset(map(int, rhs_str.split('+')))

    rules[lhs].append(rhs)

added_new = True

while added_new:
    added_new = False
    for lhs, rhses in rules.items():
        if lhs <= available:
            for rhs in rhses:
                if rhs & available != rhs:
                    available = available.union(rhs)
                    added_new = True

print(' '.join(map(str, available)))
