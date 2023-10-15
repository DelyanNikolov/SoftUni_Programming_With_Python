text = input().split()
command = input().split()
while command[0] != "3:1":
    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        elif end_index > len(text) - 1:
            end_index = len(text) - 1
        merged_text = "".join(text[start_index:end_index + 1])
        text[start_index:end_index + 1] = [merged_text]
    elif command[0] == "divide":
        current_index = int(command[1])
        partitions_count = int(command[2])
        bits_length = len(text[current_index]) // partitions_count
        divided_text = []
        for index in range(partitions_count):
            text_to_divide = text[current_index]
            if index != partitions_count - 1:
                current_bit = text_to_divide[index*bits_length:index*bits_length + bits_length]
                divided_text.append(current_bit)
            else:
                current_bit = text_to_divide[index*bits_length:]
                divided_text.append(current_bit)
        text[current_index:current_index + 1] = divided_text
    command = input().split()
print(" ".join(text))
