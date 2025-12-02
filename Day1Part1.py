zero_counter = 0
dial_pos = 50

file = open("Day1PuzzleInput.txt", "r")
for line in file:
    instruction = line.strip()
    direction = instruction[0]
    mag = int(instruction[1:])
    if direction == 'L':
        dial_pos = (dial_pos - mag) % 100
    elif direction == 'R':
        dial_pos = (dial_pos + mag) % 100
    
    if dial_pos == 0:
        zero_counter += 1

print(zero_counter)

file.close()