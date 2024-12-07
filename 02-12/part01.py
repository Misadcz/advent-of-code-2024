f = open("input.txt", "r")
safe = 0

for line in f:
    dir = 0
    arr = []
    arr = line.split()
    arr = [int(i) for i in arr]

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if (arr[i] - arr[i + 1] < 4) and (arr[i] - arr[i + 1] > 0):
                if dir == 0 or dir == -1:
                    dir = -1
                else:
                    break
            else:
                break
        else:
            if (arr[i + 1] - arr[i] < 4) and (arr[i + 1] - arr[i] > 0):
                if dir == 0 or dir == 1:
                    dir = 1
                else:
                    break
            else:
                break

        if i == len(arr) - 2:
            safe += 1
f.close()
print(safe)
