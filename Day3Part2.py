joltage_sum = 0

def find_max(input, target_length):
    highest_digit = 0
    highest_digit_index = 0

    for i in range(len(input)):
        if int(input[i]) > highest_digit and len(input) - i > target_length - 1:

            highest_digit = int(input[i])
            highest_digit_index = i 

    return highest_digit, highest_digit_index

file = open("Day3PuzzleInput.txt", "r")
for line in file:
    digit_list = []
    input = line.strip()
    index = 0
    for i in range(0, 12):
        digit, index = find_max(input, 12 - i)
        input = input[index + 1:]
        digit_list.append(digit)

    digit_string = ''.join(map(str, digit_list))
    joltage = int(digit_string)
    joltage_sum += joltage
        
print(joltage_sum)
file.close()