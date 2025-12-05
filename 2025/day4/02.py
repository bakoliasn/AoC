import sys
from functools import reduce

def main():
    with open(sys.argv[1], 'r') as file:
        done = False
        total = 0
        # build array
        layout = []

        for line in file:
            chunk = [line[j] for j in range(0, len(line), 1)]
            if chunk[len(chunk) - 1] == '\n':
                chunk.pop()
            layout.append(chunk)
        while done is not True:
            accessable = 0
            new = layout[:]

            for i in range(len(layout)):
                for j in range(len(layout[i])):
                    # center
                    if layout[i][j] == "@":
                        blocked = 0
                        # top
                        if i-1 >= 0:
                            if j-1 >= 0 and layout[i-1][j-1] == "@":
                                blocked += 1

                            if layout[i-1][j] == "@":
                                blocked += 1

                            if j+1 < len(layout[i-1]) and layout[i-1][j+1] == "@":
                                blocked += 1

                        # bottom
                        if i+1 < len(layout):

                            if j-1 >= 0 and layout[i+1][j-1] == "@":
                                blocked += 1

                            if layout[i+1][j] == "@":
                                blocked += 1

                            if j+1 < len(layout[i+1]) and layout[i+1][j+1] == "@":
                                blocked += 1

                        # left
                        if j-1 >= 0 and layout[i][j-1] == "@":
                            blocked += 1


                        # right
                        if j+1 < len(layout[i]) and layout[i][j+1] == "@":
                            blocked += 1


                        print(blocked)
                        if blocked < 4:
                            accessable += 1
                            new[i][j] = "x"
            if accessable == 0:
                done = True
            layout = new
            total += accessable
    print(total)
if __name__ == "__main__":
    main()