x = 0
y = 0
destX = 20
destY = 20

storage = []

for i in range(0, destX + 1):
    storage.append([])
    for j in range(0, destY + 1):
        storage[i].append(0);

numberOfCall = 0
numberOfAdd = 0
def numberOfRountes(x, y, destX, destY):
    global storage
    global numberOfCall
    global numberOfAdd

    numberOfCall += 1

    if x == destX or y == destY:
        return 1

    if storage[x][y] != 0:
        return storage[x][y]

    routes = numberOfRountes(x + 1, y, destX, destY) + numberOfRountes(x, y + 1, destX, destY)
    numberOfAdd += 1
    storage[x][y] = routes
    return routes

routes = numberOfRountes(x, y, destX, destY)

# print(storage)
print("numberOfAdd " + str(numberOfAdd))
print("numberOfCall " + str(numberOfCall))
print(routes)
