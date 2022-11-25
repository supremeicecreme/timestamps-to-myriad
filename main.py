input_file_name = input("Enter the name of the source file: ")
output_file_name = input("Enter the name of the output CUE file (this MUST be called the same as the audio file): ")
item_count = 1
output_file_contents = ""

with open(input_file_name, "r") as input_file:
    input_file_contents = input_file.readlines()
    for line in input_file_contents:
        if line[0] == "(":
            continue
        split_line = line.split("\u2002")
        time = split_line[0].replace("[", "").replace("]", "")
        artist, title = split_line[1].split(" - ")
        cue_block = f"ITEM {item_count} SONG\nTITLE {title}\nARTISTS {artist}\nSTART 00:{time}\n"
        item_count += 1
        output_file_contents += cue_block

print(output_file_contents)