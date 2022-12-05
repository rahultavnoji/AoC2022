stacks = [[], [], [], [], [], [], [], [], []]


def perform_instruction_on_crateMover_9000(instruction):
    for no_of_stack in range(instruction[0]):
        stacks[instruction[2]-1].append(stacks[instruction[1]-1].pop())


def perform_instruction_on_crateMover_9001(instruction):
    temp = []
    for no_of_stack in range(instruction[0]):
        temp.append(stacks[instruction[1]-1].pop())
    temp.reverse()
    stacks[instruction[2]-1].extend(temp)


def read_procedure(procedure):
    procedure = procedure.replace("move ", "")
    procedure = procedure.replace("from", "")
    procedure = procedure.replace("to", "")
    proc = list(map(int, procedure.split("  ")))
    return proc


def load_crates(crates):
    for no_of_crate, crate in enumerate(crates):
        if crate != "[0]": stacks[no_of_crate].append(crate)


def load_stack(height_of_stack, no_of_stacks, file):
    with open(file) as crates:
        stack = crates.readlines()[:height_of_stack]
        for height_of_stack in range(height_of_stack - 1, -1, -1):
            load_crates(stack[height_of_stack].replace("    ", " [0]").strip("\n").split(" "))


def top_stack(height_of_stack, no_of_stack, file):
    instruction = []
    load_stack(height_of_stack, no_of_stack, file)
    with open(file) as procs:
        procedures = procs.readlines()[height_of_stack+2:]
        for procedure in procedures:
            instruction = read_procedure(procedure)
            #perform_instruction_on_crateMover_9000(instruction)
            perform_instruction_on_crateMover_9001(instruction)

    for stack in range(no_of_stack):
        print(stacks[stack].pop())


top_stack(8, 9, "Crates")
