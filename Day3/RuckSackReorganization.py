def item_priority(item):
    if ord(item) < 97:
        return ord(item) - 64 + 26
    return ord(item) - 96


def item_in_both_compartment(items):
    first_compartment, second_compartment = items[:len(items) // 2], items[len(items) // 2:]
    return ''.join(set(first_compartment).intersection(second_compartment))


def item_with_three_elves(first_elf, second_elf, third_elf):
    return ''.join(set(first_elf).intersection(second_elf, third_elf))


def sum_of_priorities():
    total_priorities = 0
    total_priorities2 = 0
    first_elf = second_elf = third_elf = ""
    with open("List") as priority_list:
        for items in priority_list:
            total_priorities += item_priority(item_in_both_compartment(items))
            if third_elf == "":
                third_elf = second_elf
                second_elf = first_elf
                first_elf = items.strip()
            if third_elf != "":
                total_priorities2 += item_priority(item_with_three_elves(first_elf, second_elf, third_elf))
                first_elf = second_elf = third_elf = ""
    return total_priorities, total_priorities2


print(sum_of_priorities())