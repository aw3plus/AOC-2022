def p1(input_file):
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

with open("input_4.txt", "r") as f:
    # print(p1(f))
    print(p2(f))
    # print(l)

