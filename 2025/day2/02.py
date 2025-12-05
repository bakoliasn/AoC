import sys
from functools import reduce

def main():
    invalid = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            ids = line.split(',')
            for id in ids:
                first, last = id.split('-')
                for i in range(int(first), int(last) + 1):
                    code = str(i)
                    for i in range(0, len(code)):
                        if len(code) % (i+1) == 0 and i + 1 != len(code):
                            chunks = [code[j:j+i+1] for j in range(0, len(code), i + 1)]
                            if len(set(chunks)) == 1:
                                invalid.append(code)
                                break
    result = reduce(lambda x,y: int(x)+int(y), invalid)
    print(result)
if __name__ == "__main__":
    main()