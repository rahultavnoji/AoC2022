def cycle_increment(cycle, targeted_cycle, x, strength):
    if cycle == targeted_cycle:
        strength += cycle * x
        targeted_cycle += 40
        return strength, targeted_cycle
    return strength, targeted_cycle


def draw_pixel(crt, cycle, x):
    pixel_position = cycle - 1
    pixel_position = pixel_position - 40*(pixel_position//40)
    if pixel_position == x-1 or pixel_position == x or pixel_position == x+1:
        crt.append('#')
    else:
        crt.append('.')
    return crt


def cpu_signal_strength(file):
    cycle = 0
    targeted_cycle = 20
    strength = 0
    x = 1
    crt = []
    with open(file) as signals:
        for signal in signals:
            if cycle > 240:
                break
            command = signal.strip().split()
            instruction = command[0]
            if command[0] == 'addx':
                value = int(command[1])
            else:
                value = 0
            for _ in range(instruction_list.get(instruction)):
                cycle += 1
                strength, targeted_cycle = cycle_increment(cycle, targeted_cycle, x, strength)
                crt = draw_pixel(crt, cycle, x)
            x += value
    start, end = 0, 40
    for i in range(6):
        print(crt[start:end])
        start += 40
        end += 40
    return strength


instruction_list = {'noop':1, 'addx':2}
filename = "SignalStrength"
print(cpu_signal_strength(filename))