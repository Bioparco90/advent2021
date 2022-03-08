file = open("input.txt", "r")
lines = file.readlines()
file.close()

def converter(param):
    count = 0
    exponent = len(param)-1
    for bit in param:
        if bit == 1:
            count += pow(2, exponent)
        exponent -= 1
    return count

oxygenGenerator = [0] * (len(lines[0])-1)   # most commmon
co2Scrubber = [0] * (len(lines[0])-1)       # least common

#oxygen
index = 0
trueBit = 0
falseBit = 0
oxygenList = []
co2List = []

# usare whileloop per dinamicità
for _ in range(len(lines)):
    for line in lines:
        if line[index] == 1:
            trueBit += 1
        else:
            falseBit += 1
    if trueBit > falseBit or trueBit == falseBit:
        for line in lines:
            if line[index] == 1:

    index += 1

# for line in lines:
#     index = 0
#     for bit in line:
#         if bit == "1":
#             gammaRate[index] += 1
#         elif bit == "0":
#             epsilonRate[index] += 1
#         index += 1

# index = 0
# for i in gammaRate:
#     if gammaRate[index] > epsilonRate[index]:
#         gammaRate[index] = 1
#         epsilonRate[index] = 0
#     elif gammaRate[index] < epsilonRate[index]:
#         gammaRate[index] = 0
#         epsilonRate[index] = 1
#     index += 1



# gammaRate = converter(gammaRate)
# epsilonRate = converter(epsilonRate)

# print(gammaRate * epsilonRate)   
