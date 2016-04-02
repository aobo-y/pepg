x = 0
y = 0
destX = 20
destY = 20

def makeAMove(x, y, destX, destY):
    print(str(x) + " " + str(y))
    if x == destX and y == destY:
        return 1

    routes = 0
    if x < destX:
        routes += makeAMove(x + 1, y, destX, destY)
    if y < destY:
        routes += makeAMove(x, y + 1, destX, destY)
    return routes

routes = makeAMove(x, y, destX, destY)
print(routes)
