def prepare_file(file_path):
    with open(file_path, "r") as f:
        stack, moves = f.read().split("\n\n")
        moves = [x for x in moves.split("\n")]
        moves = [x.split() for x in moves]
        moves = [[int(x[1]),int(x[3]),int(x[5])] for x in moves]

    return moves, stack

def arrange(move):
    count, frm, to = move
    frm_col = stack.get(frm)
    # print(frm_col)
    to_move = frm_col[-count:]
    # print(to_move)
    del frm_col[-count:]
    # print(frm_col)
    stack[frm] = frm_col
    # print(stack)
    to_col = stack.get(to)
    # print(to_col)
    # to_move.reverse()
    to_col = to_col + to_move
    # print(to_col)
    stack[to] = to_col

    # print(stack)



def p1(moves, stack):
    result = 0
    
    lines = [x.strip() for x in input_file.read().split("\n")]
    for line in lines:
        
        ranges = [x.split("-") for x in line.split(",")]
        r1, r2 = ranges[0], ranges[1]
        r1 = [int(x) for x in r1]             
        r2 = [int(x) for x in r2]             
        
        if r1[0] <= r2[0] and r2[1] <= r1[1] or r2[0] <= r1[0] and r1[1] <= r2[1]:
            result += 1

        # print(r1, r2)
    
    return result

def p2(input_file):
    result = 0
    
    lines = [x.strip() for x in input_file.read().split("\n")]
    for line in lines:
        
        ranges = [x.split("-") for x in line.split(",")]
        r1, r2 = ranges[0], ranges[1]
        r1 = [int(x) for x in r1]             
        r2 = [int(x) for x in r2]             
        
        if not (r1[1] < r2[0] or r1[0] > r2[1]):
            result += 1
    
    return result


stack_s = {
    1 : ["Z", "N"],
    2 : ["M", "C", "D"],
    3 : ["P"]
}

#             [J] [Z] [G]            
#             [Z] [T] [S] [P] [R]    
# [R]         [Q] [V] [B] [G] [J]    
# [W] [W]     [N] [L] [V] [W] [C]    
# [F] [Q]     [T] [G] [C] [T] [T] [W]
# [H] [D] [W] [W] [H] [T] [R] [M] [B]
# [T] [G] [T] [R] [B] [P] [B] [G] [G]
# [S] [S] [B] [D] [F] [L] [Z] [N] [L]
#  1   2   3   4   5   6   7   8   9 

stack = {
    1: ["S","T","H","F","W","R"], 
    2: ["S","G","D","Q","W"], 
    3: ["B","T","W"],
    4: ["D","R","W","T","N","Q","Z","J"],
    5: ["F","B","H","G","L","V","T","Z"],
    6: ["L","P","T","C","V","B","S","G"],
    7: ["Z","B","R","T","W","G","P"],
    8: ["N","G","M","T","C","J","R"],
    9: ["L","G","B","W"]
    }

print(stack)

# 2022/inputs/sample.txt
file_name = "input_5"
file_path = f"../inputs/{file_name}.txt"
moves, _ = prepare_file(file_path)
# print(moves)
# r = p1(moves, stack)
for move in moves:
    arrange(move)
print(stack)
