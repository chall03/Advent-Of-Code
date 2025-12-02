file = open("Day2PuzzleInput.txt", "r")
input = file.read().split(',')
count = 0

for span in input:
    span = span.split('-')
    for i in range(int(span[0]), int(span[1]) + 1):
        current_id = str(i)
        id_len = len(current_id)
        if id_len % 2 == 0:
            left_half = current_id[:id_len // 2]
            right_half = current_id[id_len // 2:]

            if left_half == right_half:
                count += i

print(count)
file.close()