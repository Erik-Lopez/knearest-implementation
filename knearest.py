import matplotlib.pyplot as plt
from point import generate_points, cartesian_distance_between
from useful_stuff import index_of_smallest_value

def distance_to_all_other_points(reference_point, points):
    distances = []

    for point in points:
        distance = cartesian_distance_between(reference_point, point)
        distances.append(distance)

    return distances

def kth_nearest_items_indices(array, k):
    assert k > len(array), "Demasiados vecinos."

    nearest_neighbours_indices = []

    for _ in range(k):
        near_neighbour_index = index_of_smallest_value(array)
        nearest_neighbours_indices.append(near_neighbour_index)
        array.pop(near_neighbour_index)

    return nearest_neighbours_indices

def highest_frequency_key_value_in_dict(dictionary):
    highest_frequency_key_value = (None, float("-inf"))

    for key,val in dictionary.items():
        if val > highest_frequency_key_value[1]:
            highest_frequency_key_value = (key, val)

    return highest_frequency_key_value


def point_classification_by_knearest(point_to_classify, points, k):
    distances = distance_to_all_other_points(point_to_classify, points)
    nearest_neighbours_indices = kth_nearest_items_indices(distances, k)

    frequency_of_characteristics = {
        "True": 0,
        "False": 0
    }

    for near_neighbour_index in nearest_neighbours_indices:
        neighbour = points[near_neighbour_index]
        characteristic_value = str(neighbour[2])
        frequency_of_characteristics[characteristic_value] += 1

    highest_frequency_key_value = highest_frequency_key_value_in_dict(frequency_of_characteristics)

    classification = highest_frequency_key_value[0]
    return classification

def plot_points(points):
    plt.scatter(
        x = [point[0] for point in points],
        y = [point[1] for point in points]
    )

def main(amount_of_points, amount_of_neighbours, k):
    #points = generate_points(amount_of_points, 100)

    points1 = generate_points(amount_of_points, (10, 20), True)
    points2 = generate_points(amount_of_points, (30, 40), False)
    points = points1 + points2

    point_to_classify = generate_points(amount_of_points=1, point_range=(24, 26))[0]

    classification = point_classification_by_knearest(point_to_classify, points, k)
    point_to_classify[2] = eval(classification)

    plot_points(points1)
    plot_points(points2)
    plot_points([point_to_classify])

    plt.show()
    print(point_to_classify[2])
    
if __name__ == "__main__":
    amount_of_points = int(input("How many points? -> "))
    amount_of_neighbours = int(input("How many neighbours to check? -> "))

    main(amount_of_points, amount_of_neighbours, 3)
