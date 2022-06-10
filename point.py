import random

from useful_stuff import average

def generate_points(amount_of_points, point_range: tuple, condition = None):
    points = []

    for _ in range(amount_of_points):
        point = [random.uniform(point_range[0], point_range[1]), random.uniform(point_range[0], point_range[1]), random.choice([True, False])]
        if condition:
            point = [random.uniform(point_range[0], point_range[1]), random.uniform(point_range[0], point_range[1]), condition]

        points.append(point)

    return points

def generate_clusters(points, k):
    assert len(points) >= k, "Too many clusters, idiot."

    clusters = [random.choice(points) for _ in range(k)]

    return clusters

def average_point_position(points):
    x_average = average([point[0] for point in points])
    y_average = average([point[1] for point in points])

    return [x_average, y_average]

def cartesian_distance_between(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    return (dx**2 + dy**2)**0.5
