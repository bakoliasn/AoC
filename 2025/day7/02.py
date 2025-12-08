import sys

def main():
    with open(sys.argv[1], 'r') as file:
        timeline_counts = [1]
        timelines = [70] # 7 for test input
        for line in file:
            row = [line[i] for i in range(len(line)) if line[i] != "\n"]
            for i in range(len(row)):
                if row[i] == "^":
                    for beam in range(len(timelines)):
                        if timelines[beam] == i and timeline_counts[beam] > 0:
                            insert_count = 0
                            if beam - 1 > 0 and timelines[beam - 1] == i - 1:
                                timeline_counts[beam - 1] += timeline_counts[beam]
                            else:
                                insert_count = timeline_counts[beam]
                            if beam + 1 < len(timelines) and timelines[beam + 1] == i + 1:
                                timeline_counts[beam + 1] += timeline_counts[beam]
                            else:
                                timelines.insert(beam + 1, timelines[beam] + 1)
                                timeline_counts.insert(beam + 1, timeline_counts[beam])
                            timeline_counts[beam] = 0

                            if insert_count > 0:
                                timelines.insert(beam, timelines[beam] - 1)
                                timeline_counts.insert(beam, insert_count)

    print(sum(timeline_counts))

if __name__ == "__main__":
    main()
