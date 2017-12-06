
def solve1(arr):
    _sum = 0
    for line in arr: 
        diff = max(line) - min(line)
        _sum += diff
    print("solve1:", _sum)

import itertools
def solve2(arr):
    _sum = 0
    for line in arr:
        for a, b in itertools.product(line, line):
            if a%b == 0 and a != b:
                 # print("For line:", line,"\nA:", a, "B:", b )
                _sum += a/b
    print("solve2:", int(_sum))

_input = open("Day2/Input.txt", "r")
arr = []
for line in _input:
    arr.append(list(map(int, line.split() )))
solve1(arr)
solve2(arr)


