import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotPoints(point_cloud_data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Extract x, y, z coordinates from the point cloud data
    #x = point_cloud_data[:, 0]
    #y = point_cloud_data[:, 1]
    #z = point_cloud_data[:, 2]
    x=point_cloud_data[0]
    y=point_cloud_data[1]
    z=point_cloud_data[2]

    # Plot the point cloud
    ax.scatter(x, y, z, c='b', marker='o')

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Point Cloud Visualization')

    plt.show()
def plotPoints2D(points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Create a scatter plot to visualize the point cloud
    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, y_values, alpha=0.5)
    plt.title('Point Cloud Visualization')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    plt.show()




