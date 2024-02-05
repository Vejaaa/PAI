import itertools

def calculate_distance(city_order, distances):
    return sum(distances[city_order[i]][city_order[i + 1]] for i in range(len(city_order) - 1)) + distances[city_order[-1]][city_order[0]]

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    all_city_orders = itertools.permutations(range(num_cities))

    optimal_route, min_distance = min((city_order, calculate_distance(city_order, distances)) for city_order in all_city_orders)

    return optimal_route, min_distance

# Example usage:
cities = ["City A", "City B", "City C", "City D"]
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_route, min_distance = traveling_salesman_bruteforce(distances)

print("Optimal Route:", [cities[i] for i in optimal_route])
print("Minimum Distance:", min_distance)
