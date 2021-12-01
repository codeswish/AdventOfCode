with open("input.txt") as ifile:
    input = ifile.read().split()
    depths = [int(i) for i in input]

    windows = [(x, x + 3) for x in range(0, len(depths)) if x + 3 < len(depths)]
    depth_increases = [
        depths[x] - depths[y] for x, y in windows if 0 > depths[x] - depths[y]
    ]

print("Depth Increases: " + str(len(depth_increases)))
