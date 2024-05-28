from sklearn.cluster import DBSCAN
import numpy as np
from sklearn.preprocessing import StandardScaler


class carDetection:
    def __init__(self, cloud_points, epsilon, min_samples):
        self.points_array = np.array(cloud_points)
        #print(self.cloud_points.shape)
        self.epsilon = epsilon
        self.min_samples = min_samples
        self.detected_objects = []

    def detect_objects(self):

        self.points_array = self.points_array.reshape(-1, 1)

        clustering = DBSCAN(eps=self.epsilon, min_samples=self.min_samples).fit(self.points_array)
        #cluster_labels = clustering.fit_predict(points_array.reshape(1,-1))
        #print(self.points_array)
        labels = clustering.labels_

        # Identify unique objects based on cluster labels
        unique_labels = set(labels)

        # Group points into objects based on cluster labels
        for label in unique_labels:
            if label == -1:
                # Noise points (not assigned to any cluster)
                continue

            object_points = self.points_array[labels == label]
            self.detected_objects.append(object_points)

    def get_detected_objects(self):
        return len(self.detected_objects)



