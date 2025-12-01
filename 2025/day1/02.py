import sys

def main():
    password = 0
    last = 50
    with open(sys.argv[1], 'r') as file:
        for line in file:
            turns = int(line[1:]) // 100
            password += turns
            amount = int(line[1:]) % 100
            if (line[0:1] == 'R'):
                current = last + amount
                if (current > 99):
                    current -= 100
                    if (last != 0 and current != 0):
                        password += 1
            if (line[0:1] == 'L'):
                current = last - amount
                if (current < 0):
                    current += 100
                    if (last != 0 and current != 0):
                        password += 1
            if (current == 0):
                password += 1
            last = current
    print(password)

if __name__ == "__main__":
    main()
