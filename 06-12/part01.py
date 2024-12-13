
import time
player = [0,0,0]
counter = 0
map = []
h = 0 
w = 0

# Size of map

f = open('input.txt','r')
for line in f:
    h += 1
    w = len(line)
f.close()

map = [['0' for x in range(w+1)] for y in range(h+1)]

#Fill map + Find player

with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(h):
        for j in range(w):
            map[i][j] = lines[i][j] 
            if lines[i][j] == '^':
                player[2] = 1
                player[0] = i
                player[1] = j
            elif lines[i][j] == '>':
                player[2] = 2
                player[0] = i
                player[1] = j
            elif lines[i][j] == 'v':
                player[2] = 3
                player[0] = i
                player[1] = j
            elif lines[i][j] == '<':
                player[2] = 4
                player[0] = i
                player[1] = j
                
step = 0
while True:
    if player[2] == 1:
        if map[player[0]-1][player[1]] == '#':
            player[2] = 2
        else:
            if map[player[0]-1][player[1]] == '0':
                print('END')
                break
            map[player[0]-1][player[1]] = '^'
            map[player[0]][player[1]] = 'X'
            player[0] -= 1
    elif player[2] == 2:
        if map[player[0]][player[1]+1] == '#':
            player[2] = 3
        else:
            map[player[0]][player[1]+1] = '>'
            map[player[0]][player[1]] = 'X'
            player[1] += 1
    elif player[2] == 3:    
        if map[player[0]+1][player[1]] == '#':
            player[2] = 4
        else:
            if map[player[0]+1][player[1]] == '0':
                break
            map[player[0]+1][player[1]] = 'v'
            map[player[0]][player[1]] = 'X'
            player[0] += 1
    elif player[2] == 4:
        if map[player[0]][player[1]-1] == '#':
            player[2] = 1
        else:
            map[player[0]][player[1]-1] = '<'
            map[player[0]][player[1]] = 'X'
            player[1] -= 1
    
    # for m in map:
    #     print(m)
    # print(player)
    
  
# print(player)
f.close()
 
for m in map:
    step += m.count('X')
step += 1

print(step, ' Steps')
