def browse_filesystem(file):
    temp_dir = ""
    temp_dir_node = ""
    temp_content = []
    with open(file) as files:
        for data in files:
            if data[:4] == "$ cd":
                if temp_dir_node != "":
                    if temp_dir == "//": temp_dir = "start"
                    if temp_dir not in directories:
                        directories[temp_dir] = temp_content.copy()
                if ".." in data:
                    tmp = temp_dir.split("/")
                    tmp.pop()
                    temp_dir = "/".join(tmp)
                    continue
                temp_dir_node = data[5:-1]
                temp_dir += "/"+temp_dir_node
                temp_content.clear()
                continue
            temp_data = data.strip().split()
            if temp_data[0].isdigit():
                temp_content.append(int(temp_data[0]))
                continue
            if temp_data[0] == "dir":
                temp_content.append(temp_data[1])

    directories[temp_dir] = temp_content.copy()


def load_directory_size(node, content):
    total_size = 0
    for size in content:
        if node in directory_size:
            continue
        if type(size) is int:
            total_size += size
        else:
            if directory_size.get(size):
                total_size += directory_size[size]
            else:
                load_directory_size(node + "/" + size, directories[node + "/" + size])
                total_size += directory_size[node + "/" + size]
    directory_size[node] = total_size


def part_1():
    total_size = 0
    for directory in directory_size:
        if directory_size[directory] <= 100000:
            # print(directory)
            total_size += directory_size[directory]
    return total_size


def get_size():
    for key in directories:
        if key in directory_size:
            continue
        load_directory_size(key, directories[key])


def part_2():
    minimum = 0
    total_space_consumed = directory_size["start"]
    unused_space = 70000000 - total_space_consumed
    required_space = 30000000 - unused_space
    for directory in directory_size:
        if required_space <= directory_size[directory]:
            if minimum == 0 or minimum > directory_size[directory]:
                minimum = directory_size[directory]
    return minimum


directories = {}
directory_size = {}
browse_filesystem("FileSystem")
get_size()
print(part_1())
print(part_2())