def subset(sections):
    elf1, elf2 = sections.split(",")
    starting_section_elf1, ending_section_elf1 = map(int, elf1.split("-"))
    starting_section_elf2, ending_section_elf2 = map(int, elf2.split("-"))
    if starting_section_elf1 <= starting_section_elf2 and ending_section_elf1 >= ending_section_elf2:
        return 1
    elif starting_section_elf1 >= starting_section_elf2 and ending_section_elf1 <= ending_section_elf2:
        return 1
    return 0


def total_subset_pairs():
    subset_pairs = 0
    with open("AssignmentPairs") as assignment:
        for sections in assignment:
            subset_pairs += subset(sections.strip())
    return subset_pairs


print(total_subset_pairs())