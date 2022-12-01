with open("Advent 2022\day01input.txt") as file:
    rawInput = [eachEntry.rstrip() for eachEntry in file]

calorieGroups = []
sumGroup = []

def createCalorieGroups(calorieInput):
    tempCalorieGroup = []

    for eachSnack in calorieInput:

        if eachSnack:
            tempCalorieGroup.append(int(eachSnack))

        elif not eachSnack:
            calorieGroups.append(tempCalorieGroup)
            tempCalorieGroup = []
    
    if tempCalorieGroup:
        calorieGroups.append(tempCalorieGroup)

def createSumGroup(calorieGroupInput):
    
    for eachElf in calorieGroupInput:
        sumGroup.append(sum(eachElf))

def sortCalorieGroups(calorieGroupInput):
    return sorted(calorieGroupInput,reverse=True)

def part1Answer(sumsInput):
    return max(sumsInput)

def part2Answer(sortedSumsInput):
    return sortedSumsInput[0] + sortedSumsInput[1] + sortedSumsInput[2]

def fattestElf(sumsInput):
    return sumsInput.index(max(sumsInput)) + 1

createCalorieGroups(rawInput)
createSumGroup(calorieGroups)

print("Part 1 Answer I Hope:")
print(part1Answer(sumGroup))

print("Part 2 Answer I Hope:")
print(part2Answer(sortCalorieGroups(sumGroup)))

print("The Fattest Elf is Elf # " + str(fattestElf(sumGroup)))