# PART1
with open('input') as file:
    priorities = 0
    for line in file.readlines():
        first_part, second_part = line[:len(line) // 2], line[len(line) // 2:]
        flag = None
        for char in first_part:
            if char in second_part:
                if char.islower():
                    priorities += ord(char) - ord('a') + 1
                    flag = True
                elif char.isupper():
                    priorities += ord(char) - ord('A') + 27
                    flag = True
            if flag:
                break
print("PART1: " + str(priorities))

priorities = 0
with open('input') as file:
    rucksack = []
    counter = 0
    line_counter = 0
    rucksack.append(list())
    for line in file.readlines():
        line = line.split('\n')[0]
        rucksack[counter].append(line)
        line_counter += 1
        if line_counter == 3:
            line_counter = 0
            counter += 1
            rucksack.append(list())
    for lists in rucksack:
        if len(lists) == 3:
            flag = False
            for char in lists[0]:
                if char in lists[1]:
                    if char in lists[2]:
                        if char.islower():
                            priorities += ord(char) - ord('a') + 1
                            flag = True
                        elif char.isupper():
                            priorities += ord(char) - ord('A') + 27
                            flag = True
                if flag:
                    break

print("PART2: " + str(priorities))
