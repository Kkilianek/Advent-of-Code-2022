with open("input") as file:
    counts = 0
    for lines in file.readlines():
        first, second = lines.split(",")
        first_elements = ""
        second_elements = ""
        a, b = first.split("-")
        c, d = second.split("-")
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        for i in range(a, b + 1):
            first_elements += (str(i))
        for i in range(c, d + 1):
            second_elements += (str(i))

        if first_elements in second_elements:
            if a <= c and b >= d:
                counts += 1
            elif c <= a and d >= b:
                counts += 1
        elif second_elements in first_elements:
            if a <= c and b >= d:
                counts += 1
            elif c <= a and d >= b:
                counts += 1

print("PART1: " + str(counts))

with open("input") as file:
    counts = 0
    for lines in file.readlines():
        first, second = lines.split(",")
        first_elements = []
        second_elements = []
        a, b = first.split("-")
        c, d = second.split("-")
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        for i in range(a, b + 1):
            first_elements.append(int(i))
        for i in range(c, d + 1):
            second_elements.append(int(i))

        if set(first_elements) & set(second_elements):
            counts += 1

print("PART2: " + str(counts))
