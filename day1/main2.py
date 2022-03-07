file = open("advent.txt", "r")
lines = file.readlines()
file.close()

counter = -1
prev = 0
current = 0
index = 0

while len(lines) >= 3:
    current = int(lines[index]) + int(lines[index+1]) + int(lines[index+2])
    if current > prev:
        counter += 1
    prev = current
    lines.pop(index)

print(counter)
