import sys
from functools import reduce

def main():
    with open(sys.argv[1], 'r') as file:
        list = []
        for line in file:
            list.append(line.split())
        add = []
        for i in range(len(list[0])):
            numbers = []
            operator = None
            for j in range(len(list)):
                if list[j][i] == "*" or list[j][i] == "+":
                    operator = list[j][i]
                    break
                else:
                    numbers.append(int(list[j][i]))
            if operator == "+":
                add.append(sum(numbers))
            elif operator == "*":
                add.append(reduce(lambda x, y: x * y, numbers))
    print(sum(add))

if __name__ == "__main__":
    main()