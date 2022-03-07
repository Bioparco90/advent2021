file = open("input.txt", "r")
lines = file.readlines()
file.close()

gammaRate = [0] * (len(lines[0])-1)   # most commmon
epsilonRate = [0] * (len(lines[0])-1) # least common

for line in lines:
    index = 0
    for bit in line:
        if bit == "1":
            gammaRate[index] += 1
        elif bit == "0":
            epsilonRate[index] += 1
        index += 1

index = 0
for i in gammaRate:
    if gammaRate[index] > epsilonRate[index]:
        gammaRate[index] = 1
        epsilonRate[index] = 0
    elif gammaRate[index] < epsilonRate[index]:
        gammaRate[index] = 0
        epsilonRate[index] = 1
    index += 1

def converter(param):
    count = 0
    exponent = len(param)-1
    for bit in param:
        if bit == 1:
            count += pow(2, exponent)
        exponent -= 1
    return count

gammaRate = converter(gammaRate)
epsilonRate = converter(epsilonRate)

print(gammaRate * epsilonRate)   
