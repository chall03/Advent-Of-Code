file = open("Day4PuzzleInput.txt", "r")

lines = file.readlines()
width = len(lines[0].strip())
height = len(lines)
removed_rolls = 0
rolls_to_remove = [(0,0)]

while rolls_to_remove != []:
    rolls_to_remove = []
    for i in range(height):
        for j in range(width):
            if lines[i][j] == '@':
                adjacent_rolls = 0
                transforms = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                for transform in transforms:
                    if 0 <= i + transform[0] < height and 0 <= j + transform[1] < width:
                        if lines[i + transform[0]][j + transform[1]] == '@':
                            adjacent_rolls += 1

                if adjacent_rolls < 4:
                    removed_rolls += 1
                    rolls_to_remove.append((i, j))

    for roll in rolls_to_remove:
        replacement_line = list(lines[roll[0]])
        replacement_line[roll[1]] = '.'

        lines.insert(roll[0], replacement_line)
        lines.pop(roll[0] + 1)

print(removed_rolls)
file.close()