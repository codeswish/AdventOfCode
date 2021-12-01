with open("input.txt") as ifile:
    previous_depth = None
    depth_increases = 0

    for n, line in enumerate(ifile):
        depth = int(line)

        if previous_depth != None:
            if depth > previous_depth:
                depth_increases += 1

        previous_depth = depth


print("Depth Increases: " + str(depth_increases))
