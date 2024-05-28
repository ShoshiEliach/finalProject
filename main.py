import heapq
import subprocess
import sys

from sys import exit
import Micro
from  Micro import car
import pygame
import random
from Micro import lidar
import notIf
from Micro import points
import math
import networkx as nx
from Micro import trraficLight
from Micro import visualPoints
import datetime
import math
from Macro import get_id_and_num
from Micro import visualPoints
import datetime
import threading
import time
import ctypes
import multiprocessing
import heapQueue
from Macro import reciveBool

from heapQueue import lock
from multiprocessing import Process

#from Macro import manageGraph
from multiprocessing import Process
#יבוא קובץ בC++ והגדרת הפונקציות
lib = ctypes.CDLL("C:\\Users\\User\\Documents\\projecttt\\Threads\\main.so")
newValue=lib.addValueToList
newValue.argtypes = [ctypes.c_int]

findListById=lib.findListById
lib.findListById.argtypes = [ctypes.c_char_p]
lib.findListById.restype = ctypes.POINTER(ctypes.c_void_p)
waiters_now=lib.waiters
waiters_now.restype = ctypes.c_int
waiters_now.argtypes = [ctypes.POINTER(ctypes.c_void_p)]

addTimeToPriority=lib.updatePriority
addTimeToPriority.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
addTimeToPriority.restype = ctypes.c_int

WaitingLongTime=lib.WaitingLongTime
WaitingLongTime.restype = ctypes.c_char_p

initializeList=lib.initializeList
initializeList.argtypes = [ctypes.c_char_p]

#הגדרת תור העדיפויות של הנתיבים
pqRoads = heapQueue.PriorityQueue()
memberA1C1=heapQueue.Member("A1C1",0,0,0,True)
memberA1A2=heapQueue.Member("A1A2",0,0,0,True)
memberB1D1=heapQueue.Member("B1D1",0,0,0,True)
memberB1B2=heapQueue.Member("B1B2",0,0,0,True)
memberC1C2=heapQueue.Member("C1C2",0,0,0,True)
memberD1D2=heapQueue.Member("D1D2",0,0,0,True)
pqRoads.push(memberA1A2)
pqRoads.push(memberA1C1)
pqRoads.push(memberB1B2)
pqRoads.push(memberB1D1)
pqRoads.push(memberC1C2)
pqRoads.push(memberD1D2)

trrafics=[]
# roadsGraph=manageGraph.macroGraph
# nodes_priority_queues=manageGraph.node_priority_queues
def updateGraphFromHeapQMicro():
    temp_heap=pqRoads
    priority_queueB2=[]
    while temp_heap:
        temp_member=temp_heap.pop()
        heapq.heappush(priority_queueB2, (temp_member[1], temp_member[0]))

    heapq.heapify(priority_queueB2)
    #nodes_priority_queues['nodeB2']=priority_queueB2



def call_cpp_function(data):

    # Compile the C++ code
    subprocess.run(["g++", r"C:\Users\User\Desktop\connectToPythonWithPipe\connectToPythonWithPipe\connectToPythonWithPipe.cpp", "-o", "listenFromPython"])
    executable_path = r"C:\Users\User\Desktop\connectToPythonWithPipe\x64\Debug\connectToPythonWithPipe.exe"
    # Call the C++ executable and pass the parameters
    process = subprocess.Popen([executable_path], stdin=subprocess.PIPE)
    #print(st,num_cars)
    for d in data:
        # Send data to C++ program
        process.stdin.write(bytes(f"{d[0]} {d[1]}\n", 'utf-8'))

        process.stdin.flush()

    # Close the input pipe to signal end of input
    process.stdin.close()

    # Wait for the process to finish
    process.wait()

    # Read the output from the C++ program
    #output = process.stdout.read()
    #print(output)

    # Close the process





#פונקציה הבודקת על נתיב האם קרן הלידאר מתנגשת במכוניות שנמצאות בו אם כן מוסיפה את נקודת ההתנגשות לענן הנקודות
def identificationLidar(id,this_cars,lidar,all_points):
    this_points = []#ההתנגשויות הנוכחיות
    if any(this_cars):#אם יש מכוניות בכלל
        cloud_points = []
        #id_c_char_p = ctypes.c_char_p(id.encode())
        #waiterList = findListById(id_c_char_p)

        # עובר על כל קרן ומחשב את נקודת הסיום שלה ומצייר אותה

            #c_id = ctypes.c_void_p(waiterList)
            #print('c_id')
        # עובר על כל קרן ומחשב את נקודת הסיום שלה ומצייר אותה

        for angle in range(lidar.start_angle, lidar.end_angle + 1):
            intersect_x, intersect_y = lidar.calculate_intersection_point(angle)
            this_points.append(((intersect_x, intersect_y), lidar.position))
        all_points.extend(this_points)
        # בודק על כל רכב בנתיב האם הוא נפגש בקרן
        for i in this_points:
            x, y = i[0]
            for c in this_cars:
                  if c.collided(x, y):
                    cloud_points.append((x, y))
            if (cloud_points):
                detection = points.carDetection(cloud_points, 4, 1)
                detection.detect_objects()
                # אם הרמזור ירוק צריך להסיר את המכוניות לאחר 4 שניות
                # if not isRed:
                #     lib.countWaiters(waiterList)
                #else:
                    #מוסיף
                    #timeWait=addTimeToPriority(waiterList)
                num = detection.get_detected_objects()
                get_id_and_num.set_num_id(num,id)
                #return num              #lib.getValuesFromMicro(id,num)
                # for c in this_cars:
                #     try:
                #         print(c.vel)
                #         #       except AttributeError:
                #         #     #     print("אובייקט זה אינו מכיל את התכונה 'vel'")
                #     if c.collided(x, y):
                #         cloud_points.append((x, y))
                #     #     # עיבוד ענן הנקודות למספר הרכבים הממתינים
                # if (cloud_points):
                #     detection = points.carDetection(cloud_points, 4, 2)
                #     #
                #     detection.detect_objects()
                #         if not isRed:
                # newValue(num, waiterList)
                # mone = waiters_now(waiterList)
                # #mone=mone+timeWait
                # pqRoads.replace(id, mone)
                #כאן מעדכנים את הגרף מאקרו בערכי הצומת מיקרו
                #updateGraphFromHeapQMicro()
                #checkA1Orc1(id,mone)
                #result = [id, mone]
                #return result
            #print(x, y)


            #             lib.countWaiters(waiterList)
            #         num = detection.get_detected_objects()
            #         #num = num // 2
            #         #print(num)
            #         newValue(num, waiterList)
            #         mone = waiters_now(waiterList)
            #         pqRoads.replace(id,mone)
            #
            #         print(id, mone)
            #         result = [id, mone]
            #         # print('result')
            #         return result


#פונקציה המזמנת את זיהוי הרכבים בשביל כל רשימת הנתיבים
def process_list(data):

    list_item,all_points = data
    id,list_data,lidar,isRed = list_item

    identificationLidar(id,list_data,lidar,all_points,isRed)


def process_traffic_light(id, status):
    if status == 1:
        trrafics[id] =on_specific_trrafic(id)
    else:
        trrafics[id]=trrafics[id].off_trrafic(id)

#
# for line in sys.stdin:
#     id, status = map(int, line.strip().split())
#     process_traffic_light(id, status)
#     print("1")
#     sys.stdout.flush()


def callback(result):
    if isinstance(result, Exception):
        print(f"Error: {result}")
    else:
        print(f"Result: {result}")

#stop_thread = threading.Event()
# def checkA1Orc1(id,mone):
#   notIf.A1OrC1(id) and manageGraph.add_cars_to_graph_Road(id,mone)



#לפונקציה הזאת אני אמורה לשלוח איזה רמזור להדליק מפייתון
def on_specific_trrafic(id):
    #time.sleep(3)
    for t in trrafics:
        if t.id == id:
            t.on_trrafic()
            initializeList(id)
            #green_wave(id)
        else:
            t.off_trrafic()
def on_trrafic_head_heapQ():
    if pqRoads.first_member:
        first_member = pqRoads.first_member
        id1 = first_member.id1
        id2 = first_member.id2
        print(id1,id2)
        on_specific_trrafic(id1)
        print('1')
        on_specific_trrafic(id2)
        first_member.counter = 0
        first_member.counter1 = 0
        first_member.counter2 = 0

def diffrence_time(last,now,num_seconds):
    time_difference = last - now
    if time_difference.total_seconds() >= num_seconds:
        on_specific_trrafic(id)
        return True
    return False

def is_case_y():
    id=WaitingLongTime()
    if id !="not":
        return True,on_specific_trrafic,id
    else:
        return False,None,0


#def cars(id,num):


def traffic_light_logic():

    global is_green, elapsed_time
    elapsed_time=0
    is_green=False

    while True:
        if elapsed_time % 20 == 0:
            power_now = datetime.datetime.now()
            is_green = not is_green
        #פה צריך לבדוק את הזמן שרמזור דולק
        status, on_specific_trrafic, id = is_case_y()

        if status and is_green and diffrence_time(power_now, (datetime.datetime.now()), 10):
            is_green = False
            on_specific_trrafic(id)
        else:
            on_trrafic_head_heapQ()


        time.sleep(1)
        elapsed_time += 1


#task_thread = threading.Thread(target=repeated_task)
def callback(result):
    if isinstance(result, Exception):
        print(f"Error: {result}")
    else:
        print(f"Result: {result}")
stop_thread = threading.Event()
def check_on_trrafic():
    first_member = pqRoads.peek()
    id1 = first_member.id1
    id2 = first_member.id2
    first_member.counter = 0
    first_member.counter1 = 0
    first_member.counter2 = 0

    print(id1, id2)

    for t in trrafics:
        if t.id==id1 or t.id==id2:
            t.color=colors[1]
            t.fill(t.color)
            print(t.id)
            print('change color')
        else:
            t.color=colors[0]
            t.fill(t.color)
    task_thread.run = lambda: False
#
def define_simulation():
    print('11')
#
def repeated_task():
    stop_thread = False  # Flag to indicate thread termination
    while not stop_thread:
        # Call the function to do something
        check_on_trrafic()
        # Wait for 20 seconds before the next iteration
        time.sleep(30)
#
# # Create a thread for the repeated task
#task_thread = threading.Thread(target=repeated_task)



lib.main()
#traffic_light_thread = threading.Thread(target=traffic_light_logic)
#traffic_light_thread.start()
#task_thread.start()
colors = [(255, 0, 0), (0, 255, 0)]


max_cars = random.randrange(0, 15)
carsA = []
carsB = []
carsC = []
carsD = []


pygame.init()
pygame.display.set_caption('Smart junction')
screen = pygame.display.set_mode((800, 600))
all_points=[]
clock = pygame.time.Clock()

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #all_points = multiprocessing.Manager().list()

        #pool = multiprocessing.Pool(processes=8)
        #with multiprocessing.Pool() as pool:
            #pool.map_async(process_list, [(list_item, all_points) for list_item in lists_to_process], callback=callback, chunksize=1)

        roadAC = pygame.Surface((800, 200))
        roadAC.fill((255, 255, 0))
        roadBD = pygame.Surface((200, 600))
        roadBD.fill((0, 255, 255))

        #
        # אתחול חלון הסימולציה
        lidar1Straight = lidar.Lidar((300, 290), -100, 360, 15, 0.35)
        lidar1Right = lidar.Lidar((300, 240), -100, 360, 15, 0.35)

        lidar2Straight = lidar.Lidar((400, 200), -200, -90, 10, 0.32)
        lidar2Right = lidar.Lidar((470, 200), -200, -90, 10, 0.32)

        lidar3Straight = lidar.Lidar((500, 310), -100, 180, 10, 0.35)
        lidar3Right = lidar.Lidar((500, 370), -100, 180, 10, 0.35)

        lidar4Straight = lidar.Lidar((330, 400), -200, 90, 10, 0.32)
        lidar4Right = lidar.Lidar((400, 400), -200, 90, 10, 0.32)
        trraficA1 = trraficLight.trraficWithPyg("A1", 20, 50, colors[0], 300, 220)
        trraficA1.fill(trraficA1.color)

        trraficA2 = trraficLight.trraficWithPyg("A2", 20, 50, colors[0], 300, 290)
        trraficA2.fill(trraficA2.color)

        trraficB1 = trraficLight.trraficWithPyg("B1", 20, 50, colors[0], 330, 550)
        trraficB1.fill(trraficB1.color)

        trraficB2 = trraficLight.trraficWithPyg("B2", 20, 50, colors[0], 400, 550)
        trraficB2.fill(trraficB2.color)

        trraficC1 = trraficLight.trraficWithPyg("C1", 20, 50, colors[0], 530, 280)
        trraficC1.fill(trraficC1.color)

        trraficC2 = trraficLight.trraficWithPyg("C2", 20, 50, colors[0], 530, 350)
        trraficC2.fill(trraficC2.color)

        trraficD1 = trraficLight.trraficWithPyg("D1", 20, 50, colors[0], 400, 120)
        trraficD1.fill(trraficD1.color)

        trraficD2 = trraficLight.trraficWithPyg("D2", 20, 50, colors[0], 470, 120)
        trraficD2.fill(trraficD2.color)

        trrafics = [trraficA1, trraficA2, trraficB1, trraficB2, trraficC1, trraficC2, trraficD1, trraficD2]

        screen.blit(roadAC, (0, 200))
        screen.blit(roadBD, (300, 0))
        screen.blit(trraficA1, (trraficA1.x, trraficA1.y))
        screen.blit(trraficA2, (trraficA2.x, trraficA2.y))
        screen.blit(trraficB1, (trraficB1.x, trraficB1.y))
        screen.blit(trraficB2, (trraficB2.x, trraficB2.y))
        screen.blit(trraficC1, (trraficC1.x, trraficC1.y))
        screen.blit(trraficC2, (trraficC2.x, trraficC2.y))
        screen.blit(trraficD1, (trraficD1.x, trraficD1.y))
        screen.blit(trraficD2, (trraficD2.x, trraficD2.y))

        #לקבל את מס' הרכבים שצריך להוסיף מהסימולציה
        reciveBool.boolean_values[0] and carsA.append(car.car(0.0, (random.randrange(200, 400))))

        reciveBool.boolean_values[1] and carsB.append(car.car((random.randrange(300, 490)), 0.0))
        reciveBool.boolean_values[2] and carsC.append(car.car(800.0, (random.randrange(200, 400))))
        reciveBool.boolean_values[3] and carsD.append(car.car((random.randrange(300, 490)), 600.0))

            # הסעת הרכבים כל עוד הרמזור ירוק
        for c in carsA:
            if trraficA1.get_at((0, 0)) == (255, 0, 0) and c.x >= 250:
                c.vel = 0
            c.x += c.vel
            pygame.draw.rect(screen, (255, 0, 0), (c.x, c.y, c.width, c.height))

        for c in carsB:
            if trraficB1.get_at((0, 0)) == (255, 0, 0) and c.y >= 250:
                c.vel = 0
            c.y += c.vel
            pygame.draw.rect(screen, (255, 0, 0), (c.x, c.y, c.width, c.height))

        for c in carsC:
            if trraficC1.get_at((0, 0)) == (255, 0, 0) and c.x <= 500:
                c.vel = 0
            c.x -= c.vel
            pygame.draw.rect(screen, (255, 0, 0), (c.x, c.y, c.width, c.height))

        for c in carsD:
            if trraficD1.get_at((0, 0)) == (255, 0, 0) and c.y <= 400:
                c.vel = 0
            c.y -= c.vel
            pygame.draw.rect(screen, (255, 0, 0), (c.x, c.y, c.width, c.height))

        for i in range(len(all_points) - 1):
            # print((points[i], points[i + 1]), (points[i + 2][0], points[i + 2][1]))
            x1, y1 = all_points[i][0]

            # Extract the x and y coordinates for the ending point
            x2, y2 = all_points[i][1]

            pygame.draw.line(screen, (128, 0, 128), (x1, y1), (x2, y2))

            # for list_item in lists_to_process:
            # pool.map_async(process_list, ((list_item,points),), callback=callback, chunksize=2)
            # pool.map_async(process_list, [(list_item, points) for list_item, points, _ in lists_to_process],
            # callback=callback, chunksize=2)
        numA1=identificationLidar("A1", carsA, lidar1Straight,all_points)
        numA2=identificationLidar("A2", carsA, lidar1Right,all_points)
        numB1=identificationLidar("B1", carsB,lidar2Straight,all_points)
        numB2=identificationLidar("B2", carsB, lidar2Right,all_points)
        numC1=identificationLidar("C1", carsC,lidar3Straight,all_points)
        numC2=identificationLidar("C2", carsC, lidar3Right,all_points)
        numD1=identificationLidar("D1", carsD, lidar4Straight,all_points)
        numd2=identificationLidar("D2", carsD, lidar4Right,all_points)
        data = [
            ("A1",numA1),
            ("A2", numA2),
            ("B1", numB1),
            ("B2", numB2),
            ("C1", numC1),
            ("C2", numC2),
            ("D1", numD1),
            ("D2",numd2)
        ]

        #call_cpp_function(data)
        lists_to_process = [("A1", carsA, lidar1Straight, trraficA1.trrafic_is_red()),
                            ("A2", carsA, lidar1Right, trraficA2.trrafic_is_red()),
                            ("B1", carsB, lidar2Straight, trraficB1.trrafic_is_red()),
                            ("B2", carsB, lidar2Right, trraficB2.trrafic_is_red()),
                            ("C1", carsC, lidar3Straight, trraficC1.trrafic_is_red()),
                            ("C2", carsC, lidar3Right, trraficC2.trrafic_is_red()),
                            ("D1", carsD, lidar4Straight, trraficD1.trrafic_is_red()),
                            ("D2", carsD, lidar4Right, trraficD2.trrafic_is_red())]
        pygame.display.update()
        clock.tick(60)



        # הוספת הרכבים לכביש באופן אקראי ורנדומלי


    # pool.close()
    # pool.join()
















