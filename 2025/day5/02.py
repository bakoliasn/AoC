import sys
from functools import reduce

def main():
    with open(sys.argv[1], 'r') as file:
        ranges = []
        valid = []
        for line in file:
            if(line == "\n"):
                break
            if line[-1:] == "\n":
                line = line[:-1]
            ranges.append(line)
        ranges.sort()
        for r in ranges:
            first, last = r.split("-")
            pop = []
            for i in range(len(valid)):
                valid_first, valid_last = valid[i]
                if (int(first) >= int(valid_first) and int(first) <= int(valid_last)) or (int(last) >= int(valid_first) and int(last) <= int(valid_last)):
                    first = min(int(first), int(valid_first))
                    last = max(int(last), int(valid_last))
                    pop.append(i)
            for index, p in enumerate(pop):
                valid.pop(p - index)
            valid.append([int(first), int(last)])
        print(sum([last - first + 1 for first, last in valid]))
if __name__ == "__main__":

    main()