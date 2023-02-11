import random 

# the chromosome struct is necessary in order to access to its genes and fitness attributes
class Chromosome: 
    def __init__(self, genes, fitness=None):
        self.genes = genes
        self.fitness = fitness

def generateChromosomes(min, max, num_chromonomes):
    chromosomes = []
    for i in range(num_chromonomes):
        size = random.randint(min, max)
        genes = [random.randint(0,1) for _ in range(size)]
        chromosomes.append(Chromosome(genes))
    return chromosomes

def generateFitness(chromosomes):
    for c in chromosomes:
        c.fitness = random.random()

def getScheme():
    scheme = input("Ingrese al esquema H a evaluar:")
    return scheme

def getProbability(chromosomes):
    probabilities = []
    total_fitness = sum([c.fitness for c in chromosomes])
    for c in chromosomes:
        p = c.fitness/total_fitness
        probabilities.append(p)
    return probabilities

def generateRandomInteger(min, max):
    number = random.randint(min,max)
    return number

def getOrdenAndLongitude(scheme):
    orden = 0
    for i in range(len(scheme)):
        if scheme[i] == "H":
            order += 1  
    length = len(scheme)
    return (orden, length)

if __name__ == "__main__":
    min = 5
    max = 10    
    num_chromosomes = 50
    chromosomes = generateChromosomes(min, max, num_chromosomes)
    scheme = getScheme()
    generateFitness(chromosomes)
    probabilities = getProbability(chromosomes)
    scheme = getScheme()
    orden, longitude = getOrdenAndLongitude(scheme)
    generateFitness(chromosomes)
    probabilities = getProbability(chromosomes)
    print("Chromosomes: ", chromosomes)
    print("Scheme: ", scheme)
    print("Orden: ", orden)
    print("Longitude: ", longitude)
    print("Probabilities: ", probabilities)

