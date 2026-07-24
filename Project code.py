import random
import math 


# Function to create a random set of cities with coordinates ( only can be used once )
def create_random_cities(num_cities):
    cities = {f"City{i}": (random.uniform(0, 100), random.uniform(0, 100)) for i in range(1, num_cities + 1)}
    return cities

# Function to calculate the distance between two cities
def calc_distance(city1, city2, cities):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate the total distance of a route
def calculate_total_distance(route, cities):
    total_distance = sum(calc_distance(route[i], route[i + 1], cities) for i in range(len(route) - 1))
    total_distance += calc_distance(route[-1], route[0], cities)
    return total_distance

# Function to calculate the fitness score of an individual (negative total distance)
def calculate_fitness_score(individual, cities):
    total_distance = calculate_total_distance(individual, cities)
    fitness_score = -total_distance
    return fitness_score

# Function to create a random individual (permutation of city names)
def create_individual(city_names):
    individual = city_names.copy()
    random.shuffle(individual)
    return individual

# Genetic Algorithm function
def genetic_algorithm(cities, population_size, mutation_rate, num_generations):
    city_names = list(cities.keys())
    best_solution = None
    best_distance = float('inf')
    # intial population
    for _ in range(num_generations):
        population = [create_individual(city_names) for _ in range(population_size)]

        for individual in population:
            distance = calculate_total_distance(individual, cities)
            if distance < best_distance:
                best_solution = individual
                best_distance = distance

        parents = population[:int(0.2 * population_size)]
        offspring = parents.copy()
        # crossover
        while len(offspring) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            crossover_point = random.randint(1, len(city_names) - 1)
            child = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
            offspring.append(child)
        # mutation 
        for i in range(int(0.2 * population_size), population_size):
            if random.random() < mutation_rate:
                swap_indices = random.sample(range(len(city_names)), 2)
                offspring[i][swap_indices[0]], offspring[i][swap_indices[1]] = offspring[i][swap_indices[1]], offspring[i][swap_indices[0]]

    return best_solution, best_distance

# Main function
def main():
    print("Traveling Salesman Problem With Genetic Algorithm")
    print("-------------------------------------------")
    # defining number of cities 
    num_cities = 25
    cities = create_random_cities(num_cities)
    # user inputs for genetic alg parameter
    population_size = int(input("Enter population size: "))
    mutation_rate = float(input("Enter mutation rate as a percentage (e.g., 1 for 1%): ")) / 100
    num_generations = int(input("Enter the number of generations: "))

    best_solution, total_distance = genetic_algorithm(cities, population_size, mutation_rate, num_generations)
    fitness_score = calculate_fitness_score(best_solution, cities)
    
    print("Best Solution:", best_solution)
    print(f"Total Distance: {total_distance:.2f} miles")
    print(f"Fitness Score: {fitness_score:.2f} miles")
# ensures the code runs
if __name__ == "__main__":
    main()
