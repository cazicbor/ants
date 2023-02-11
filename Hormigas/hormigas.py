import random, sys, math

# Generates a symmetric matrix for size n*n, filled up with random floating values bewteen 0 and 1
def matrixDistance(n, maxDistance): 
    matrix = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(i):
            matrix[i][j] = maxDistance*random.random()
            matrix[j][i] = matrix[i][j]

    return matrix


# Picks an ant's path, knowing the distances and the pheromones while eliminating the visited ones 
def pickPath(distances, pherom, visited):
    weights = []
    available = []
    current = visited[-1]

    # Influence of each value:
    # alpha: pheromones
    # beta: distance
    alpha = 0.1
    beta = 0.5

    # The beta parameter (weight of the distances) is 0.5, alpha is 0.1
    for i in range(len(distances)):
        if i not in visited:
            p = math.pow((1.0 + pherom[current][i]), alpha)
            w = math.pow(1.0/distances[current][i], beta) * p
            available.append(i)
            weights.append(w)

    # Pick randomly one of the available paths, knowing its relative weight
    value = random.random() * sum(weights)
    acumulated = 0.0
    i = -1
    while value > acumulated:
        i += 1
        acumulated += weights[i]

    return available[i]


# Generates an ant, that will pick a path knowing the distances and the pheromones track
# Returns a tuple with the way and its length
def pickWay(distances, pheromones):
    # The initial path always has the 0 index
    way = [0]
    length = 0 

    # Pick each weight depending on distances and pheromones
    while len(way) < len(distances):
        path = pickPath(distances, pheromones, way)
        length += distances[way[-1]][path]
        way.append(path)

    # For termination, we need to return the path of origin (0)
    length += distances[way[-1]][0]
    way.append(0)

    return (way, length)

# todo
def pheromonesTrack(pheromones, way, dose):
    for i in range(len(way) - 1):
        pheromones[way[i]][way[i+1]] += dose


# todo
def evaporatePheromones(pheromones):
    for l in pheromones:
        for i in range(len(l)):
            l[i] *= 0.9

#todo
def ants(distances, iterations, midDistance):
    # todo
    n = len(distances)
    pheromones = [[0 for i in range(n)] for j in range(n)]

    # todo
    bestWay = []
    lengthBestWay = sys.maxsize

    # todo
    for iter in range(iterations):
        (way, lengthtWay) = pickWay(distances, pheromones)

        if lengthtWay <= lengthBestWay:
            bestWay = way
            lengthBestWay = lengthtWay
        
        pheromonesTrack(pheromones, way, midDistance/lengthtWay)

        #todo
        evaporatePheromones(pheromones)

    #todo
    return (bestWay, lengthBestWay)

# todo
numberOfPaths = 10
maxDistance = 10 
paths = matrixDistance(numberOfPaths, maxDistance)

# Obtaining the best path
iterations = 1000
midDistance = numberOfPaths*maxDistance/2
(way, lengthWay) = ants(paths, iterations, midDistance)
print("Way: ", way)
print("Way length: ", lengthWay)



