f = open("input.txt", "r")
results = []
equations = []
for line in f:
    results.append(int(line.split(":")[0]))
    line = line.split(":")[1].strip()
    line = line.split(" ")
    for i in range(len(line)):
        line[i] = int(line[i])
    equations.append(line)
f.close()


def calculate(equation, target, current=None):
    if not current:
        current = equation[0]
        equation = equation[1:]

    if not equation:
        return current == target

    return calculate(equation[1:], target, current + equation[0]) or calculate(equation[1:], target, current * equation[0])


sum = 0
for i in range(len(results)):
    if calculate(equations[i], results[i]):
        sum += results[i]

print(sum)
