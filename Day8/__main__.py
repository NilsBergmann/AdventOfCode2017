from collections import defaultdict
import operator as op

_input = open("Day8/Input.txt", "r")
registers = defaultdict(int)
comparisons = {'>': op.gt, '<': op.lt, '>=': op.ge, '<=': op.le, '!=': op.ne, '==': op.eq}
_max = float('-inf')
for line in _input:
    register, operation, amount, _, compA, compOp, compB  = line.split()
    if comparisons[compOp](registers[compA], int(compB)):
        if operation == "inc":
            registers[register] += int(amount)
        else:
            registers[register] -= int(amount)
    _max = max(_max, registers[register])
print("MAX:", max(registers.values()), "All time MAX:", _max)


    