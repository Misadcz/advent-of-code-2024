f = open("input.txt", "r")
sum = 0
left_arr = []
right_arr = []
for line in f:
    left, right = line.split()
    left_arr.append(left)
    right_arr.append(right)
f.close()

left_arr.sort()
right_arr.sort()

for i in range(len(left_arr)):
    if left_arr[i] > right_arr[i]:
        sum += (int(left_arr[i]) - int(right_arr[i]))
    else:
        sum += (int(right_arr[i]) - int(left_arr[i]))

print(sum)