file = open("input.txt", "r")
lines = file.readlines()
file.close()

horizontal = 0
depth = 0

for line in lines:
    direction = line.split()[0]
    movement = int(line.split()[1])
    if direction == "forward":
        horizontal += movement
    elif direction == "up":
        depth -= movement
    elif direction == "down":
        depth += movement

print(horizontal*depth)
