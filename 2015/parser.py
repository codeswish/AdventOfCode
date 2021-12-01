STORE = {"basement": False, "count": 0}


def set_basement(x):
    if not STORE["basement"]:
        STORE["basement"] = True
        STORE["count"] = x


def parse(input=""):
    count = 0

    for n in range(0, len(input)):
        char = input[n]

        if char == "":
            count += 0

        if char == "(":
            count += 1

        if char == ")":
            count += -1

        if count == -1:
            set_basement(n + 1)

    return count


if __name__ == "__main__":
    import sys
    from pathlib import Path

    ifile = sys.argv[1]
    # Read in file passed as an argument
    # Call parse on file contents
    # Print the count to the console
    contents = Path(ifile).read_text()
    data = parse(contents)

    print(data)
    if STORE["basement"]:
        print("Basement entered at position " + str(STORE["count"]))
