file = open("Day2PuzzleInput.txt", "r")
input = file.read().split(',')
count = 0

for span in input:
    span = span.split('-')
    for i in range(int(span[0]), int(span[1]) + 1):
        current_id = str(i)
        id_len = len(current_id)
        if id_len % 2 == 0:
            max_seq_len = id_len / 2
            for i in range(1, int(max_seq_len) + 1):
                chunked_id = [current_id[j:j + i] for j in range(0, id_len, i)]
                if(len(set(chunked_id)) == 1):
                    count += int(current_id)
                    break
        elif id_len % 2 == 1:
            max_seq_len = id_len / 3
            for i in range(1, int(max_seq_len) + 1):
                chunked_id = [current_id[j:j + i] for j in range(0, id_len, i)]
                if(len(set(chunked_id)) == 1):
                    count += int(current_id)
                    break

print(count)
file.close()