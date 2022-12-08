def prepare_file(file_path):
    with open(file_path, "r") as f:
        lines = f.read().split("\n")    
        lines = [x for x in lines if x not in ["$ ls"]]

        # print(lines)

    return lines

# 2022/inputs/sample.txt
file_name = "sample"
file_path = f"../inputs/{file_name}.txt"
lines = prepare_file(file_path)
# print(makers)

threshold = 100000
dirs = {}
current_dir = "root"
current_files = []
inc = 1
i = 0

for line in lines:
    pline = lines[i-1]
    if line == "$ cd ..": inc = 1
    if "$ cd" in line and line != "$ cd .." and line != "$ cd /":
        if pline == "$ cd ..":
            print("fuck")
            inc = 1
        else:
            current_dir = line[-1:] + str(inc)
            inc += 1
            current_files = []
    
    if line[0].isdigit():
        current_files.append(int(line.split()[0]))
        dirs[current_dir] = current_files
    
    i += 1
 
print(dirs)
    