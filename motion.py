# horn and schunk

# lucas and kanade
def compute_R(dx, dy, dt):
    rxx = 0
    rxy = 0
    ryy = 0
    rxt = 0
    ryt = 0

    # compute rxx and ryy
    for x in range(len(dx)):
        for y in range(len(dx[0])):
            rxx += dx[x][y] ** 2
            ryy += dy[x][y] ** 2

    # compute rxy, rxt, ryt
    for x in range(len(dx)):
        for y in range(len(dx[0])):
            rxy += dx[x][y] * dy[x][y]
            rxt += dx[x][y] * dt[x][y]
            ryt += dy[x][y] * dt[x][y]

    print('rxx = ' + str(rxx))
    print('rxy = ' + str(rxy))
    print('ryy = ' + str(ryy))
    print('rxt = ' + str(rxt))
    print('ryt = ' + str(ryt))


# main
dx = [
    [0, 0, 0],
    [0.5, 0, -0.5],
    [0, 0, 0]
]

dy = [
    [0, 0.5, 0],
    [0, 0, 0],
    [0, -0.5, 0]
]

dt = [
    [0, 0, 0],
    [0, -1, 1],
    [0, 0, 0]
]

compute_R(dx, dy, dt)
