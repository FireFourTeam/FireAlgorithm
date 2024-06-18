import sys
input = sys.stdin.read

def arr(N, heights):
    arrows = [0] * (max(heights) + 1)
    arrow_count = 0

    for height in heights:
        if arrows[height] > 0:
            arrows[height] -= 1
            arrows[height - 1] += 1
        else:
            arrow_count += 1
            arrows[height - 1] += 1

    return arrow_count

data = input().split()
N = int(data[0])
heights = list(map(int, data[1:]))

print(arr(N, heights))
