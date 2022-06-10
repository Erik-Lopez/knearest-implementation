import matplotlib.pyplot as plt
import os

def index_of_smallest_value(array):
    smallest_element = [0, float("inf")]

    for idx,element in enumerate(array):
        if element < smallest_element[1]:
            smallest_element[0] = idx
            smallest_element[1] = element
    
    return smallest_element[0] 

def average(X):
    return sum(X) / len(X)

def plot(points, clusters, should_show_images=False, should_save_images=False):
    points_x_values = [point[0] for point in points]
    points_y_values = [point[1] for point in points]

    clusters_x_values = [cluster[0] for cluster in clusters]
    clusters_y_values = [cluster[1] for cluster in clusters]

    plt.scatter(x = points_x_values, y=points_y_values)
    plt.scatter(x = clusters_x_values, y=clusters_y_values)

    if should_show_images:
        plt.show()
    
    if should_save_images:
        i = 0
        if not os.path.exists("./plots/"):
            os.mkdir("./plots/")

        while os.path.exists(f"./plots/image-{i}.png"):
            i += 1

        plt.savefig(f"./plots/image-{i}.png")
