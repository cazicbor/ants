import random
import math

# First, let's define each function that we want to maximize
def f1(x):
    return 1 - (x-(1/2))**2

def f2(x):
    return 36 - ((6*x - 3)**2 - 3)**2

def f3(x):
    return 1 - (x-(1/2))**6

def f4(x):
    return 10

def f5(x):
    return math.sin(4*math.pi*x)**2

# Generates a random individual (a list of random values)
def generateRandomIndividual(length):
    return [random.uniform(0, 1) for _ in range(length)]

# Performs mutation on an individual by randomly changing some of its values
def mutate(individual, mutationProbability):
    for i in range(len(individual)):
        if random.uniform(0, 1) < mutationProbability:
            individual[i] = random.uniform(0, 1)
    return individual

# Performs crossover (recombination) on two individuals to create a new one
def crossover(indiv1, indiv2, prob):
    if random.random() < prob:
        position = 0
        child = [0.0] * len(indiv1)
        child[position] = (indiv1[position] + indiv2[position]) / 2
        return child
    else:
        return random.choice([indiv1, indiv2])

# Evaluates the fitness of an individual based on the target function
def evaluateFitness(function, individual):
    return function(individual[0])

# Main genetic algorithm to find the maximum for a given target function
def geneticAlgorithm(f, populationSize, mutationProb, crossoverProb, generations):
    population = [[random.random()] for i in range(populationSize)]
    for i in range(generations):
        population.sort(key=lambda x: -f(x[0]))
        if f(population[0][0]) == 1:
            break
        population = population[:populationSize//2]
        while len(population) < populationSize:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2, crossoverProb)
            if random.random() < mutationProb:
                child[0] = random.random()
            population.append(child)
    population.sort(key=lambda x: -f(x[0]))
    return population[0][0]


res1 = geneticAlgorithm(f1, 100, 0.005, 0.5, 200)
print("Maximum of f1 :", res1)

res2 = geneticAlgorithm(f2, 100, 0.005, 0.5, 200)
print("Maximum of f2 :", res2)

res3 = geneticAlgorithm(f3, 100, 0.005, 0.5, 200)
print("Maximum of f3 :", res3)

res4 = geneticAlgorithm(f4, 100, 0.005, 0.5, 200)
print("Maximum of f4 :", res4)

res5 = geneticAlgorithm(f5, 100, 0.005, 0.5, 200)
print("Maximum of f5 :", res5)


# Let's test our algorithm's performance with a new function:
def f6(x):
    return math.sqrt(x)*2*x

res6 = geneticAlgorithm(f6, 100, 0.005, 0.5, 200)
print("Maximum of f6 :", res6)