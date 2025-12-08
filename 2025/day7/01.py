import sys

def main():
    with open(sys.argv[1], 'r') as file:
        splits = 0
        beams = set([])
        for line in file:
            row = [line[i] for i in range(len(line)) if line[i] != "\n"]
            
            for i in range(len(row)):
                if row[i] == "S":
                    beams.add(i)
                elif row[i] == "^" and i in beams:
                    splits += 1
                    beams.remove(i)
                    beams.update([i-1, i+1])
        
    print(splits)


if __name__ == "__main__":
    main()