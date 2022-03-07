file = open("input.txt", "r")
lines = file.readlines()
file.close()

horizontal = 0
depth = 0
aim = 0

for line in lines:
    direction = line.split()[0]
    movement = int(line.split()[1])
    if direction == "forward":
        horizontal += movement
        depth += (aim * movement)
    elif direction == "up":
        aim -= movement
    elif direction == "down":
        aim += movement

print(horizontal*depth)
