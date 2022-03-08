file = open("input.txt", "r")
lines = file.readlines()
file.close()

oxygenGenerator = []
co2Scrubber = []
for _ in lines:
    oxygenGenerator.append(_)
    co2Scrubber.append(_)

#oxygen
for i in range(len(lines[0])):
    if len(oxygenGenerator) == 1:
        break

    checkBit = [elem[i] for elem in oxygenGenerator]
    if checkBit.count("1") >= len(checkBit)/2:
        commonBit = "1"
    else:
        commonBit = "0"

    oxygenGenerator = [elem for elem in oxygenGenerator if commonBit == elem[i]]

# CO2
for i in range(len(lines[0])):
    if len(co2Scrubber) == 1:
        break

    checkBit = [elem[i] for elem in co2Scrubber]
    if checkBit.count("1") >= len(checkBit)/2:
        leastCommonBit = "0"
    else:
        leastCommonBit = "1"

    co2Scrubber = [elem for elem in co2Scrubber if leastCommonBit == elem[i]]

# Final
print(int(oxygenGenerator[0], 2) * int(co2Scrubber[0], 2))
