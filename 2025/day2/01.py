import sys
from functools import reduce

def main():
    invalid = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            ids = line.split(',')
            for id in ids:
                first, last = id.split('-')
                for i in range(int(first), int(last)):
                    code = str(i)
                    if len(code) % 2 == 0:
                        middle = len(code) // 2
                        if code[:middle] == code[middle:]:
                            invalid.append(code)
    result = reduce(lambda x,y: int(x)+int(y), invalid)
    print(result)
if __name__ == "__main__":
    main()