def calculate_calories(calories):
    max, backup1, backup2 = 0, 0, 0
    for calorie in calories:
        if max < calorie:
            backup2 = backup1
            backup1 = max
            max = calorie
        elif backup1 < calorie:
            backup2 = backup1
            backup1 = calorie
        elif backup2 < calorie:
            backup2 = calorie
    return max, max+backup1+backup2


def get_calories():
    elves = []
    with open("Day1/Calories") as calories_list:
        elve = 0
        calories = calories_list.readlines()
        for calorie in calories:
            if calorie.strip():
                elve = elve + int(calorie)
                continue
            elves.append(elve)
            elve = 0
    return elves


if __name__ == '__main__':
    calories = get_calories()
    maximum_calorie, total_backup_calorie = calculate_calories(calories)
    print(maximum_calorie)
    print(total_backup_calorie)