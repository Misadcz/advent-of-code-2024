w = 0
h = 0
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        w = len(line)
        h += 1
f.close()    
arr = [[0 for x in range(w+5)] for y in range(h+5)]

for i in range(h+5):
    for j in range(w+5):
        arr[i][j] = "."
        

with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(h):
        for j in range(w):
            arr[i][j] = lines[i][j] 
f.close()

counter = 0

for i in range(h):
    for j in range(w):
        if arr[i][j] == "X":
            #RIGHT
            if arr[i][j] == "X" and arr[i][j+1] == "M" and arr[i][j+2] == "A" and arr[i][j+3] == "S":
                counter += 1
            #LEFT
            if arr[i][j] == "X" and arr[i][j-1] == "M" and arr[i][j-2] == "A" and arr[i][j-3] == "S":
                counter += 1
            #DOWN
            if arr[i][j] == "X" and arr[i+1][j] == "M" and arr[i+2][j] == "A" and arr[i+3][j] == "S":
                counter += 1
            #UP
            if arr[i][j] == "X" and arr[i-1][j] == "M" and arr[i-2][j] == "A" and arr[i-3][j] == "S":
                counter += 1
            #RIGHT DOWN
            if arr[i][j] == "X" and arr[i+1][j+1] == "M" and arr[i+2][j+2] == "A" and arr[i+3][j+3] == "S":
                counter += 1
            #RIGHT UP
            if arr[i][j] == "X" and arr[i-1][j+1] == "M" and arr[i-2][j+2] == "A" and arr[i-3][j+3] == "S":
                counter += 1
            #LEFT DOWN
            if arr[i][j] == "X" and arr[i+1][j-1] == "M" and arr[i+2][j-2] == "A" and arr[i+3][j-3] == "S":
                counter += 1
            #LEFT UP
            if arr[i][j] == "X" and arr[i-1][j-1] == "M" and arr[i-2][j-2] == "A" and arr[i-3][j-3] == "S":
                counter += 1
print(counter)