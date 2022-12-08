def prepare_file(file_path):
    with open(file_path, "r") as f:
        makers = f.read().split("\n")
        makers = [list(x) for x in makers]
    
    return makers

# 2022/inputs/sample.txt
file_name = "input_6"
file_path = f"../inputs/{file_name}.txt"
makers = prepare_file(file_path)
# print(makers)

for maker in makers:
    i = 0
    l = []
    for m in maker:
        l = maker[i:i+14]
        # print(l)
        done = len(set(l)) == len(l)
        # print(done)
        i += 1
        if done: break


    print(i + 13, l)
    # break 
    