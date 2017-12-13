def solve1(arr):
    _index = 0
    stepCount = 0
    while _index < len(arr):
        offset = arr[_index]
        arr[_index] += 1
        _index += offset
        if _index < 0:
            _index = 0
        stepCount += 1
    print(stepCount)

def solve2(arr):
    _index = 0
    stepCount = 0
    while _index < len(arr):
        offset = arr[_index]
        if offset >= 3:
            arr[_index] -= 1
        else:
            arr[_index] += 1
        _index += offset
        if _index < 0:
            _index = 0
        stepCount += 1
    print(stepCount)
    
from copy import deepcopy 
_input = open("Day5/Input.txt", "r")
arr = []
for line in _input:
    arr.append(int(line))
solve1(deepcopy(arr))
solve2(deepcopy(arr))