from copy import deepcopy
def solve1(arr):
    seenArrays = [deepcopy(arr)]
    while True:
        index = arr.index(max(arr))
        maxValue = arr[index]
        arr[index] = 0
        for _ in range(maxValue):
            index = (index+1) % len(arr)
            arr[index]+=1
        if arr in seenArrays: 
            break
        seenArrays.append(deepcopy(arr))
    print(len(seenArrays))

_input = open("Day6/Input.txt", "r")
arr = list(map(int, _input.readline().split()))
solve1(arr)