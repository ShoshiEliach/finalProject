import math
from Micro import points
import asyncio


import ctypes


# Link Python libraries

# Load the shared library
#lib = ctypes.CDLL('./counter.so')  # Provide the path to the compiled shared library

# Define the argument and return types for the C++ function
#lib.process_values.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
#lib.process_values.restype = None

# Example array of values




class Lidar:
    def __init__(self, position,range, angle,num_rays,reduce_factor):
        self.position = position
        self.num_rays = num_rays
        self.range = range
        self.angle = angle
        self.cloud_points=[]
        self.start_angle = angle - 7
        self.end_angle = angle + 7
        self.reduce_factor = reduce_factor
        self.detected_now_object=[]
        self.cars_mone=0
    def create_rays(self):



        rays=[]
        angular_step=float(self.range/self.num_rays)
        for i in range(self.num_rays):
            x = self.position[0] + i * math.cos(i * angular_step)
            y = self.position[1] + i * math.sin(i * angular_step)
            z=1
            ray_direction = (x, y)
            point=(x,y,z)
            self.cloud_points.append(point)

            rays.append(ray_direction)

            #print(len(detected_cars))
            #print("Detected Objects:")
            #for idx, obj in enumerate(detected_cars):
                #print(f"Object {idx + 1}: {obj}")

        #return rays
        return rays



    def calculate_intersection_point(self,angle):
        angle_radians = math.radians(angle)
        x_increment = 800 * self.reduce_factor * math.cos(angle_radians)
        y_increment = 600 * self.reduce_factor * math.sin(angle_radians)

        intersect_x = self.position[0] - x_increment
        intersect_y = self.position[1] + y_increment

        return intersect_x, intersect_y

    async def add_cars(self,value):

        self.detected_now_object.append(value)

    async def process_car(self):
        index = 0
        #while True:
        if index < len(self.detected_now_object):
            x = self.detected_now_object[index]  # Get the value at the current index
            self.cars_mone = self.cars_mone + x
            await asyncio.sleep(4.6875)
            self.cars_mone = self.cars_mone - x
        else:
            await asyncio.sleep(1)

    async def manage_lidar1(self,values):
        process = asyncio.ensure_future(self.process_car())
        add = asyncio.ensure_future(self.add_cars(values))
        await asyncio.gather(add, process)
        print(self.cars_mone)
    def manage_lidar2(self):
        values = self.detected_now_object
        arr = (ctypes.c_int * len(values))(*values)

        start_index = self.cars_mone  # Starting from index 2

        # Call the C++ function with the starting index
        #lib.process_values(arr, len(values), start_index)

        # Get the current value of mone
        print(f"Current mone value from C++: {lib.mone}")




