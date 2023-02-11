import random


class Particle:
    # Constructor used to initialize a particle's instance with its attributes: position, velocity and best position 
    def __init__(self, pos_range, vel_range):
        self.position = [random.uniform(pos_range[0], pos_range[1]) for i in range(len(pos_range))] # pos_range and vel_range are tuples defining the range of position and velocity, 
        # so the position is a random int between [pos_range[0], pos_range[1]]
        self.velocity = [random.uniform(vel_range[0], vel_range[1]) for i in range(len(pos_range))]
        self.best_pos = self.position.copy() # initially, a best particule's best position is its initial position

class Swarm:
    # Constructor
    def __init__(self, num_particles, x_range, v_range, iterations, fitness):
        self.N = num_particles
        self.particles = [Particle(x_range, v_range) for i in range(self.N)]
        self.best_global_pos = [0.0 for i in range(self.N)]
        self.iterations = iterations
        self.alpha = 1.4
        self.beta_c = 2.0
        self.beta_s = 2.0
        self.fitness_fn = fitness

    def optimize(self):
        for i in range(self.iterations):
            for particle in self.particles:
                for j in range(len(particle.position)):
                    particle.velocity[j] = self.alpha * particle.velocity[j] + self.beta_c * random.random() * (particle.best_pos[j] - particle.position[j]) + self.beta_s * random.random() * (self.best_global_pos[j] - particle.position[j])
                    particle.position[j] += particle.velocity[j]
                if self.fitness_fn(particle.position) < self.fitness_fn(particle.best_pos):
                    particle.best_pos = particle.position.copy()
                if self.fitness_fn(particle.position) < self.fitness_fn(self.best_global_pos):
                    self.best_global_pos = particle.position.copy()
        return self.best_global_pos, [particle.velocity for particle in self.particles], [particle.best_pos for particle in self.particles]

def fitness(position):
    return random.random()


num_iterations = int(input("Enter the number of iterations: "))

swarm = Swarm(10, [-5, 5], [-5, 5], 100, fitness)
best_global_pos, velocities, best_particle_pos = swarm.optimize()

print("best_global_pos: ", best_global_pos)
print("velocities: ", velocities)
print("best_particle_pos: ", best_particle_pos)