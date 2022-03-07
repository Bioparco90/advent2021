file = open("advent.txt", "r")
lines = file.readlines()
file.close()

counter = -1
prev = 0
for line in lines:
    if int(line) > prev:
        counter += 1
    prev = int(line)

print(counter)
