file = open("Day4PuzzleInput.txt", "r")

lines = file.readlines()
width = len(lines[0].strip())
height = len(lines)
accessible_rolls = 0

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
                accessible_rolls += 1

print(accessible_rolls)
file.close()