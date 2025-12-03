joltage_sum = 0
max_joltage = 0

file = open("Day3PuzzleInput.txt", "r")
for line in file:
    input = line.strip()
    for i in range(len(input) - 1):
        first_digit = int(input[i])
        for j in range(i + 1, len(input)):
            second_digit = int(input[j])
            if int(str(first_digit) + str(second_digit)) > max_joltage:
                max_joltage = int(str(first_digit) + str(second_digit))
    joltage_sum += max_joltage
    max_joltage = 0

print(joltage_sum)
file.close()