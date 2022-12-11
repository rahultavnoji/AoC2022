def perform_round(inspection, items, operation, test, rounds, lcm):
    for monkey in range(len(items)):
        inspect = 0
        for item_number in range(len(items.get(monkey))):
            second_operand = 0
            worry = items.get(monkey)[0]
            items.get(monkey).remove(items.get(monkey)[0])
            if operation.get(monkey)[1] == 'old':
                second_operand = worry
            else:
                second_operand = operation.get(monkey)[1]
            if operation.get(monkey)[0] == '+':
                worry += second_operand
            elif operation.get(monkey)[0] == '-':
                worry -= second_operand
            elif operation.get(monkey)[0] == '*':
                worry *= second_operand
            else:
                worry /= second_operand
            if rounds == 20:
                worry //= 3
            else:
                worry %= lcm
            if worry % test.get(monkey)[0] == 0:
                items[test.get(monkey)[1]].append(worry)
            else:
                items[test.get(monkey)[2]].append(worry)
            inspect += 1
        inspection[monkey] = inspection.get(monkey) + inspect
    return inspection


def monkey_business(file_name, part):
    inspection = {}
    items = {}
    operation = {}
    test = {}
    rounds = 0
    if part == 'part1':
        rounds = 20
    else:
        rounds = 10000
    with open(file_name) as mnkeys:
        monkeys = mnkeys.readlines()
        for monkey in range(0, len(monkeys), 7):
            monkey_number = int(monkeys[monkey].rstrip().split()[1][0])
            monkey += 1
            items[monkey_number] = [int(x) for x in monkeys[monkey].replace('Starting items: ', '').rstrip().split(', ')]
            monkey += 1
            operation[monkey_number] = monkeys[monkey].replace('Operation: new = old ', '').rstrip().split()
            if operation.get(monkey_number)[1] != 'old':
                operation.get(monkey_number)[1] = int(operation.get(monkey_number)[1])
            monkey += 1
            test[monkey_number] = []
            test[monkey_number].append(int(monkeys[monkey].replace('Test: divisible by ', '').rstrip()))
            monkey += 1
            test[monkey_number].append(int(monkeys[monkey].rstrip().split()[-1]))
            monkey += 1
            test[monkey_number].append(int(monkeys[monkey].rstrip().split()[-1]))
            inspection[monkey_number] = 0
    lcm = 1
    for i in test.values():
        lcm *= i[0]
    for _ in range(rounds):
        inspection = perform_round(inspection, items, operation, test, rounds, lcm)
        # print(inspection)
    max_1 = max_2 = 0
    for inspect in inspection.values():
        if max_1 < inspect:
            max_2 = max_1
            max_1 = inspect
        if max_1 > inspect > max_2:
            max_2 = inspect
    print(max_1*max_2)


monkey_business('puzzle', 'part1')
monkey_business('puzzle', 'part2')
