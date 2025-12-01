import sys

def main():
    password = 0
    current = 50
    with open(sys.argv[1], 'r') as file:
        for line in file:
            amount = int(line[1:]) % 100
            if (line[0:1] == 'R'):
                current += amount
                if (current > 99):
                    current -= 100
            if (line[0:1] == 'L'):
                current -= amount
                if (current < 0):
                    current += 100
            if (current == 0):
                password += 1
    print(password)

if __name__ == "__main__":
    main()