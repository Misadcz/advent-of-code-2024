
rules = {}
updates = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if '|' in line:
            key, value = map(int, line.split('|'))
            if key in rules:
                rules[key].append(value)
            else:
                rules[key] = [value]
        elif ',' in line:
            lst = []
            for i in line.split(','):
                lst.append(int(i))
            updates.append(lst)
        else:
            continue

def checkRules(update, index, rule):
    # print(update, update[index], rule)
    for r in rule:
        if r in update[:index]:
            return False
    return True
        

sum = 0
for update in updates:
    check = 1
    for i in range(len(update)):
        if update[i] in rules:
            if checkRules(update,i, rules[update[i]]) == False:
                check = 0
                break
            else:
                check = 1
                continue
    if check == 1:
        length = int(len(update) / 2)
        sum += update[length]
print(sum)
        
        
        
