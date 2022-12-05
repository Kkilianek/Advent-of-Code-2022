my_choices = []
oponent_choices = []

lines = 0
with open('input') as file:
    for line in file.readlines():
        oponent_selection = line.split(" ")[0]
        oponent_choices.append(oponent_selection)
        my_choice = line.split(" ")[1].split('\n')[0]
        my_choices.append(my_choice)
        lines += 1


# LEGEND:
# A,X: ROCK (1 point)
# B,Y: PAPER (2 points)
# C,Z: SCISSORS (3 points)

def part1():
    points = 0
    for i in range(lines):
        if my_choices[i] == 'X':  # ROCK
            points += 1
            if oponent_choices[i] == "A":  # ROCK
                points += 3
            elif oponent_choices[i] == "C":  # SCISSORS
                points += 6
        if my_choices[i] == 'Y':  # PAPER
            points += 2
            if oponent_choices[i] == "B":  # PAPER
                points += 3
            elif oponent_choices[i] == "A":  # ROCK
                points += 6
        elif my_choices[i] == 'Z':  # SCISSORS
            points += 3
            if oponent_choices[i] == "C":  # SCISSORS
                points += 3
            elif oponent_choices[i] == "B":  # PAPER
                points += 6
    print("Part1: " + str(points))


# LEGEND V2
# X: LOSE
# Y: DRAW
# Z: WIN

def part2():
    points = 0
    for i in range(lines):
        if my_choices[i] == 'X':  # MUST LOSE
            if oponent_choices[i] == "A":  # SELECT SCISSORS
                points += 3
            elif oponent_choices[i] == "B":  # SELECT ROCK
                points += 1
            elif oponent_choices[i] == "C":  # SELECT PAPER
                points += 2
        if my_choices[i] == 'Y':  # MUST DRAW, SELECT THE SAME
            points += 3
            if oponent_choices[i] == "A":
                points += 1
            elif oponent_choices[i] == "B":
                points += 2
            elif oponent_choices[i] == "C":
                points += 3
        elif my_choices[i] == 'Z':  # MUST WIN, SELECT WINNING OPTION
            points += 6
            if oponent_choices[i] == "A":  # SELECT PAPER
                points += 2
            elif oponent_choices[i] == "B":  # SELECT SCISSORS
                points += 3
            elif oponent_choices[i] == "C":  # SELECT ROCK
                points += 1
    print("Part2: " + str(points))


part1()
part2()
