from copy import copy

file = open("input.txt", "r")
lines = file.readlines()
file.close()

oxygen_diagnostics = copy(lines)

for i in range(len(lines[0])):
    if len(oxygen_diagnostics) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in oxygen_diagnostics]
    common_bit = '1' if all_entries_at_pos.count('1') >= len(oxygen_diagnostics)/2 \
                 else '0'
    oxygen_diagnostics = [entry for entry in oxygen_diagnostics 
                                    if entry[i]==common_bit]
oxygen_rating = int(oxygen_diagnostics[0], base=2)
print('oxygen', oxygen_diagnostics[0], oxygen_rating)