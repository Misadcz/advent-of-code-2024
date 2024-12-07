# read file in python

with open("input.txt", "r") as f:
    line = f.read()
sum = 0


def pairBracketIndexes(line, index):
    if line[index] == "(":
        left = index
        right = index + 1
        counter = 1
        while counter > 0:
            right += 1
            if right >= len(line):
                break
            elif line[right] == "(":
                counter += 1
            elif line[right] == ")":
                counter -= 1
        return True, left, right
    return False, -1, -1


def isNum(line):
    for i in line:
        if not i.isdigit():
            return False
    return True


def isItRealMul(line):
    if line.count(",") > 1 or line.count(",") < 1:
        return False
    else:
        index = line.find(",")
        if isNum(line[:index]) and isNum(line[index + 1 :]):
            return True


def getNum(line):
    if isNum(line):
        return int(line)
    return -1

action = 1
for i in range(0, len(line)):
    if (
        line[i] == "d"
        and line[i + 1] == "o"
        and line[i + 2] == "("
        and line[i + 3] == ")"
    ):
        action = 1
    elif (
        line[i] == "d"
        and line[i + 1] == "o"
        and line[i + 2] == "n"
        and line[i + 3] == "'"
        and line[i + 4] == "t"
        and line[i + 5] == "("
        and line[i + 6] == ")"
    ):
        action = 0
    isPair, left, right = pairBracketIndexes(line, i)
    if isPair:
        if (
            (line[left - 1] == "l")
            and (line[left - 2] == "u")
            and (line[left - 3] == "m")
        ):
            if isItRealMul(line[left + 1 : right]):
                index = line.find(",", left + 1)
                left = getNum(line[left + 1 : index])
                right = getNum(line[index + 1 : right])
                result = left * right
                if result > 0 and action == 1:
                    sum += result

print(sum)
