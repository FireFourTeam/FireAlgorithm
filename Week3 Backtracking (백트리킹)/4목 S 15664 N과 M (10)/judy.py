import itertools

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()


for comb in itertools.combinations_with_replacement(numbers, M):
    print(' '.join(map(str, comb)))
