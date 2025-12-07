import sys

def main():
    with open(sys.argv[1], 'r') as file:
        ranges = []
        ids = []
        target = "ranges"
        for line in file:
            if(line == "\n"):
                target = "ids"
                continue
            if line[-1:] == "\n":
                line = line[:-1]
            if target == "ranges":
                ranges.append(line)
            elif target == "ids":
                ids.append([0, line])
            
        for i in range(len(ids)):
            for valid in ranges:
                first, last = valid.split("-")
                if int(ids[i][1]) >= int(first) and int(ids[i][1]) <= int(last):
                    ids[i][0] = 1
        print(sum([v for v, _ in ids]))
if __name__ == "__main__":
    main()