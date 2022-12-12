data = [s.strip() for s in open("heightmap").readlines()]
width = len(data[0])
height = len(data)


def h(xy):
    return data[xy[1]][xy[0]]


def adj(xy1, xy2):
    return ord(h(xy1)) <= ord(h(xy2)) + 1


def getCoordsAndReplace(sym, newsym):
    sy = min([y for y in range(height) if sym in data[y]])
    sx = data[sy].index(sym)
    data[sy] = data[sy][:sx] + newsym + data[sy][sx + 1:]
    return (sx, sy)


def getNeighbours(xy):
    nbrs = []
    (x, y) = xy
    if x > 0 and adj(xy, (x - 1, y)): nbrs.append((x - 1, y))
    if x < width - 1 and adj(xy, (x + 1, y)): nbrs.append((x + 1, y))
    if y > 0 and adj(xy, (x, y - 1)): nbrs.append((x, y - 1))
    if y < height - 1 and adj(xy, (x, y + 1)): nbrs.append((x, y + 1))
    return nbrs


(sx, sy) = getCoordsAndReplace('S', 'a')
(ex, ey) = getCoordsAndReplace('E', 'z')
olist = [(ex, ey)]
clist = []
steps = 0

while ((sx, sy) not in olist):
    steps += 1
    newolist = []
    for xy in olist:
        for n in getNeighbours(xy):
            if n not in olist and n not in clist and n not in newolist:
                newolist.append(n)
        clist.append(xy)
    olist = newolist

print("PART 1: Steps: ", steps)

olist = [(ex, ey)]
clist = []
steps = 0

while 'a' not in [h(xy) for xy in olist]:
    steps += 1
    newolist = []
    for xy in olist:
        for n in getNeighbours(xy):
            if n not in olist and n not in clist and n not in newolist:
                newolist.append(n)
        clist.append(xy)
    olist = newolist

print("PART 2: Steps: ", steps)
