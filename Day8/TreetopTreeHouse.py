def get_row_column(file):
    with open(file) as forest:
        for tree_rows, tree_row in enumerate(forest):
            pass
    return tree_rows+1, len(tree_row)


def load_trees(file):
    with open(file) as forest:
        copter = forest.readlines()
        for tree_row in range(row):
            trees[tree_row] = list((copter[tree_row].strip()))


def process_visibility():
    n_visible = 0
    max_score = 0
    visibility = False
    for i in range(0,row):
        for j, tree_size in enumerate(trees[i]):
            if i == 0 or i == row - 1 or j == 0 or j == column - 1:
                n_visible += 1
                continue
            else:
                visibility, tmp = check_visibility(i, j)
                if max_score < tmp:
                    max_score = tmp
                if visibility:
                    n_visible += 1
    print(n_visible, max_score)


def check_visibility(i, j):
    top = bottom = right = left = "visible"
    sc_top = sc_bottom = sc_right = sc_left = 0
    visibility = False
    for inc in range(1, i+1):
        if trees[i][j] <= trees[i-inc][j] and top == "visible":
            top = "not_visible"
            sc_top = inc
            break
        sc_top = inc
    for inc in range(1, row-i):
        if trees[i][j] <= trees[i+inc][j] and bottom == "visible":
            bottom = "not_visible"
            sc_bottom = inc
            break
        sc_bottom = inc
    for inc in range(1, j+1):
        if trees[i][j] <= trees[i][j-inc] and left == "visible":
            left = "not_visible"
            sc_left = inc
            break
        sc_left = inc
    for inc in range(1, column-j):
        if trees[i][j] <= trees[i][j+inc] and right == "visible":
            right = "not_visible"
            sc_right = inc
            break
        sc_right = inc
    if top == bottom == left == right == "not_visible":
        visibility = False
    else:
        visibility = True
    return visibility, sc_right * sc_top * sc_left * sc_bottom


file_name = "Trees"
row, column = get_row_column(file_name)
trees = [[0] * column for i in range(row)]
load_trees(file_name)
process_visibility()