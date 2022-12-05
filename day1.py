elves = list()

with open('input') as file:
    calories = 0
    for line in file:
        if line == '':
            elves.append(calories)
            break
        elif line == '\n':
            elves.append(calories)
            calories = 0  # reset calories if there is '/n' char
        else:
            line = line.strip('\n')
            calories += int(line)

elves.sort()
print(elves[-1])
print(sum(elves[-3:]))
