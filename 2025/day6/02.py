import sys
from functools import reduce

def main():
    with open(sys.argv[1], 'r') as file:
        table = []
        for line in file:
            table.append([line[i] for i in range(len(line)) if line[i] != "\n"])
        add = []
        numbers = []
        operator = None
        
        for col in range(len(table[0])):
            done = True
            col_num = ""
            
            for row in range(len(table)):
                if table[row][col] != " ":
                    done = False
                    if table[row][col] == "+" or table[row][col] == "*":
                        operator = table[row][col]
                    else:
                        col_num += table[row][col]

            if col == len(table[0]) -1:
                done = True                
            if len(col_num) > 0:
                numbers.append(int(col_num))
            if done is True:
                if operator == "+":
                    add.append(sum(numbers))
                elif operator == "*":
                    add.append(reduce(lambda x, y: x * y, numbers))
                operator = None
                numbers = []
    print(sum(add))

if __name__ == "__main__":
    main()