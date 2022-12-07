import string

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

def p1(input_file):
    result = 0
    ix = 0
    lines = input_file.read().split("\n")
    len(lines)

    for line in line:
        ix += 1

        line_len = int(len(line)/2)
        a = list(line[:line_len])
        b = list(line[-line_len:])

        common = [i for i in a if i in b]
        try:
            score = string.ascii_lowercase.index(common[0]) + 1
        except:
            score = string.ascii_uppercase.index(common[0]) + 27

        result += score
        # print(a, b, common, score)
    
    return result

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def p2(input_file):
    result = 0
    lines = input_file.read().split("\n")

    for ls in chunker(lines, 3):

        # print(ls[0], ls[1], ls[2])

        common = list(set(ls[0]).intersection(ls[1], ls[2]))
        print(common)
        try:
            score = string.ascii_lowercase.index(common[0]) + 1
        except:
            score = string.ascii_uppercase.index(common[0]) + 27

        result += score

    
    return result

with open("input_3.txt", "r") as f:
    r = p2(f)
    print(r)
    # l.sort(reverse=True)
    # print(l[0] + l[1] + l[2] )

