import sys
from functools import reduce

def main():
    with open(sys.argv[1], 'r') as file:
        batteries = []
        for line in file:
            max = (0,0)
            second = (0,0)
            chunks = [line[i:i+1] for i in range(0, len(line), 1)]
            if chunks[len(chunks) - 1] == '\n':
                chunks.pop()
            for index, battery in enumerate(chunks):
                if int(battery) > int(max[1]) and index != len(chunks) -1:
                    max = (index, battery)
                    second = (0,0)
                elif index > int(max[0]) and int(battery) > int(second[1]):
                    second = (index, battery)
            batteries.append(f"{max[1]}{second[1]}")
    result = reduce(lambda x,y: int(x)+int(y), batteries)
    print(result)

if __name__ == "__main__":
    main()