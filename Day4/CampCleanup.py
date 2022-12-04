def subset(elf1, elf2):
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        return 1
    elif elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        return 1
    return 0


def overlap(elf1, elf2):
    if elf1[0] <= elf2[0] <= elf1[1]:
        return 1
    elif elf2[0] <= elf1[0] <= elf2[1]:
        return 1
    return 0


def total_subset_pairs():
    subset_pairs = 0
    overlap_pairs = 0
    with open("AssignmentPairs") as assignment:
        for sections in assignment:
            elf1, elf2 = sections.strip().split(",")
            elf1, elf2 = list(map(int, elf1.split("-"))), list(map(int, elf2.split("-")))
            subset_pairs += subset(elf1, elf2)
            overlap_pairs += overlap(elf1, elf2)
    return subset_pairs, overlap_pairs


print(total_subset_pairs())