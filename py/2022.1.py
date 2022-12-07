def p1a(input_file):
    return max(sum(int(i) for i in x.split()) for x in input_file.read().split("\n\n"))

def p1b(input_file):
    return [sum(int(i) for i in x.split()) for x in input_file.read().split("\n\n")]

with open("input_1.txt", "r") as f:
    l = p1b(f)
    # print(l)
    l.sort(reverse=True)
    print(l[0] + l[1] + l[2] )

