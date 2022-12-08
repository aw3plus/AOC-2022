import numpy as np

def perpare_file(file_path):
    with open(file_path, "r") as f:
        lines = f.read().split("\n")
        lines = [[int(x) for x in list(a)] for a in lines]

    return lines

file_name = "sample"
file_path = f"../inputs/{file_name}.txt"
lines = perpare_file(file_path)
trees = np.array(lines)
print("trees.shape", trees.shape)
seen = np.full(trees.shape, 0)

# print(seen)

for r in range(trees.shape[0]):
    for c in range(trees.shape[1]):
        if trees[r][c] > trees[r][c-1]:
            seen[r][c] = 1
        elif trees[r][c] > trees[r-1][c]:
            seen[r][c] = 1
        # if trees[r][c] >= trees[r+1][c]:
        #     break
        # elif trees[r][c] >= trees[r][c+1]:
        #     break

# trees = np.flip(trees)
# seen = np.flip(seen)
# for r in range(trees.shape[0]):
#     for c in range(trees.shape[1]):
#         if trees[r][c] > trees[r][c-1] and seen[r][c] == 0:
#             seen[r][c] = 1
#         elif trees[r][c] > trees[r-1][c] and seen[r][c] == 0:
#             seen[r][c] = 1

seen[:, 0] = 1
seen[0, :] = 1
seen[:, trees.shape[1]-1] = 1
seen[trees.shape[0]-1, :] = 1

# print(trees)
# print(seen)

print(np.sum(seen))
