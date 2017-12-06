
def solve1(number):
    sum = 0 
    for digit, nextDigit in zip(number, number[1:]):
        if digit==nextDigit:
            sum += int(digit)
    if number[0] == number[-1]:
        sum += int(number[0])
    print("solve 1:", sum)

def solve2(number):
    sum = 0
    for index ,digit in enumerate(number):
        matchingIndex = int((index+(len(number)/2))%len(number))
        if digit == number[matchingIndex]:
            sum += int(digit)
    print("solve 2:", sum)

_input = open("Day1/Input.txt", "r")
for line in _input:
    solve1(line)
    solve2(line)


