zero_counter = 0
dial_pos = 50

file = open("Day1PuzzleInput.txt", "r")
for line in file:
    instruction = line.strip()
    direction = instruction[0]
    mag = int(instruction[1:])

    while mag > 100:
        mag -= 100
        zero_counter += 1
    if direction == 'L':
        pre_mod_dial_pos = dial_pos - mag
        if pre_mod_dial_pos < 0 and dial_pos != 0:
            zero_counter += 1
        dial_pos = pre_mod_dial_pos % 100
        if dial_pos == 0:
            zero_counter += 1
    elif direction == 'R':
        pre_mod_dial_pos = dial_pos + mag
        if pre_mod_dial_pos > 100 and dial_pos != 0:
            zero_counter += 1
        dial_pos = pre_mod_dial_pos % 100
        if dial_pos == 0:
            zero_counter += 1

print(zero_counter)

file.close()