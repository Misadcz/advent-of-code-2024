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
    if i == 0:
        continue
    for j in range(w):
        if arr[i][j] == "A":
            if (arr[i-1][j-1] == 'M' and arr[i+1][j+1] == 'S') or (arr[i-1][j-1] == 'S' and arr[i+1][j+1] == 'M'):
                if (arr[i-1][j+1] == 'M' and arr[i+1][j-1] == 'S') or (arr[i-1][j+1] == 'S' and arr[i+1][j-1] == 'M'):
                    counter += 1
            
print(counter)