d = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
}

win = {
    "A X" : None,
    "A Y" : True,
    "A Z" : False,
    "B X" : False,
    "B Y" : None,
    "B Z" : True,
    "C X" : True,
    "C Y" : False,
    "C Z" : None,
}

lookup = {
    "A X" : 3,
    "A Y" : 4,
    "A Z" : 8,

    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,

    "C X" : 2,
    "C Y" : 6,
    "C Z" : 7,
}

# A: Rock 1
# B: Paper 2
# C: Scissors 3

win = {
    "X" : False,
    "Y" : None,
    "Z" : True
}

def score3(should_win, op_choice):
    result = win.get(should_win)
    match result:
        case True:
            match op_choice:
                case A:
                    return 6 + d.get("Y")
            match op_choice:
                case B:
                    return 6 + d.get("Z")
            match op_choice:
                case C:
                    return 6 + d.get("X")
        case False:
            match op_choice:
                case A:
                    return 0 + d.get("Z")
            match op_choice:
                case B:
                    return 0 + d.get("X")
            match op_choice:
                case C:
                    return 0 + d.get("Y")
        case None:
            match op_choice:
                case A:
                    return 3 + d.get("X")
            match op_choice:
                case B:
                    return 3 + d.get("Y")
            match op_choice:
                case C:
                    return 3 + d.get("Z")

def score2(game):
    result = win.get(game)
    match result:
        case True:
            return 6
        case False:
            return 0
        case None:
            return 3

def score(x,y):
    if x == "A" and y == "X":
        return 3 + d.get(x)
    elif x == "A" and y == "Y":
        return 0 + d.get(x)
    elif x == "A" and y == "Z":
        return 6 + d.get(x)
    elif x == "B" and y == "X":
        return 6 + d.get(x)
    elif x == "B" and y == "Y":
        return 3 + d.get(x)
    elif x == "B" and y == "Z":
        return 0 + d.get(x)
    elif x == "C" and y == "X":
        return 0 + d.get(x)
    elif x == "C" and y == "Y":
        return 6 + d.get(x)
    elif x == "C" and y == "Z":
        return 3 + d.get(x)

def p1(input_file):
    result = 0
    for line in input_file.read().split("\n"):
        # print(line)
        x,y = line.split()
        choice_score = d.get(y)
        if choice_score is None:
            print(line, x,y)
        assert choice_score is not None, "choice was None"
        # print(x,y, score3(y, x))
        result = result + score3(y, x)
        # print(result)
    
    return result

def p2(input_file):
    result = 0
    for line in input_file.read().split("\n"):
        result += lookup.get(line)

    return result
    

with open("input_2.txt", "r") as f:
    result = p2(f)
    # print(l)
    # l.sort(reverse=True)
    print(result)

