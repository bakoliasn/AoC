import sys
from functools import reduce

def main():
    with open(sys.argv[1], 'r') as file:
        batteries = []
        for line in file:
            on = [(0,0) for _ in range(12)]
            chunks = [line[i:i+1] for i in range(0, len(line), 1)]
            if chunks[len(chunks) - 1] == '\n':
                chunks.pop()
            for index, battery in enumerate(chunks):
                for i, charge in enumerate(on):
                    if int(battery) > charge[1] and index + 11 - i < len(chunks):
                        current = (index, int(battery))
                        part1 = on[:i]
                        part2 = [(0,0) for _ in range(11 - i)]
                        on = [*part1, current, *part2]
                        break
            batteries.append("".join([str(amount) for _, amount in on]))
    result = reduce(lambda x,y: int(x)+int(y), batteries)
    print(result)
    
if __name__ == "__main__":
    main()