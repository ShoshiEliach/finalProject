from asyncio import sleep

import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque
from multiprocessing import Process, Queue
import asyncio
import heapQueue
from Macro import roadAxis
macroGraph=nx.DiGraph()
nodes_list = ['nodeA1','nodeA2','nodeA3','nodeA4','nodeB1','nodeB2','nodeB3','nodeB4','nodeC1','nodeC2','nodeC3','nodeC4']

macroGraph.add_nodes_from(nodes_list)
edge_list = [('nodeA1', 'nodeA2', 9), ('nodeA2', 'nodeA3', 8),('nodeA3','nodeA4',7), ('nodeB1', 'nodeB2',4), ('nodeB2', 'nodeB3', 6), ('nodeB3', 'nodeB4', 5), ('nodeC1', 'nodeC2',7), ('nodeC2', 'nodeC3', 6), ('nodeC3', 'nodeC4',9),
             ('nodeA1','nodeB1',4), ('nodeA2','nodeB2',5), ('nodeA3','nodeB3',2), ('nodeA4','nodeB4',3), ('nodeB1', 'nodeC1',6), ('nodeB2', 'nodeC2',5), ('nodeB3', 'nodeC3',4), ('nodeB4', 'nodeC4',3)]
for edge in edge_list:
    macroGraph.add_edge(edge[0], edge[1], weight=edge[2])
# Mapping of identifiers to numerical values
identifier_mapping = {'A1C1': 0, 'A1A2': 0, 'B1D1': 0, 'B1B2': 0, 'C1C2': 0, 'D1D2': 0}
roadAxisGraph=roadAxis.RoadAxisManager(macroGraph)
# מאתחל תורי עדיפויות לכל הצמתים
node_priority_queues = {}
nodes_st_lists={}
for node in nodes_list:
    #יוצר לכל צומת תור עדיפויות משלה
    priority_queue = []
    #יוצרת לכל צומת רשימת נתיבים משלה
    st_list=[('A1',0),('A2',0),('B1',0),('B2',0),('C1',0),('C2',0),('D1',0),('D2',0)]
    # צור תור עדיפות עם מזהים ומשקלים עבור כל צומת
    for key, value in identifier_mapping.items():
        identifier = key
        heapq.heappush(priority_queue, (value, identifier))

    heapq.heapify(priority_queue)

    node_priority_queues[node] = priority_queue
    nodes_st_lists[node] = st_list
# Example of accessing the priority queue for 'nodeA'
print("Priority queue for node 'nodeA1':", node_priority_queues['nodeA1'])
# Draw the graph
pos = nx.spring_layout(macroGraph)
edge_labels = {(u, v): d['weight'] for u, v, d in macroGraph.edges(data=True)}

nx.draw(macroGraph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(macroGraph, pos, edge_labels=edge_labels)

plt.show()

def get_value_by_id_node(node_value, target_id):
    if node_value in node_priority_queues:
        priority_queue = node_priority_queues[node_value]
        for priority, identifier in priority_queue:
            if identifier == target_id:
                return priority
    return None
transitions_node={
    "nodeA1":{
        "C2":"nodeA2",
        "B2":"nodeB1"
    },
    "nodeA2":{
        "C2":"nodeA3",
        "B2":"nodeB2"
    },
    "nodeA3":{
        "C2":"nodeA4",
        "B2":"nodeB3"
    },
    "nodeA4":{
        "B2":"nodeB4"
    },
    "nodeB1":{
        "C2":"nodeB2",
        "B2":"nodeC1"
    },
    "nodeB2":{
        "C2":"nodeB3",
        "B2":"nodeC2"
    },
    "nodeB3":{
        "C2":"nodeB4",
        "B2":"nodeC3"
    },
    "nodeB4":{
        "B2":"nodeC4"
    },
    "nodeC1":{
        "C2":"nodeC2"
    },
    "nodeC2":{
        "C2":"nodeC3"
    },
    "nodeC3":{
        "C2":"nodeC4"
    }
}
transitions_st = {
    "nodeA2": {
        "nodeA1": "A1"

    },
    "A3": {
        "nodeA2": "A1"
    },
    "A4":{
        "nodeA3": "A1"
    },
    "B1": {
        "nodeA1": "D1"
    },
    "B2": {
        "nodeB1": "A1",
        "nodeA2": "D1",
    },
    "nodeB3": {
        "nodeB2": "A1",
        "nodeA3": "D1"
    },
    "nodeB4": {
        "nodeA4": "D1",
        "nodeB3":"A1"
    },
    "nodeC1":{
        "nodeB1":"D1"
    },
    "nodeC2": {
        "nodeC1": "A1",
        "nodeB2":"D1"
    },

    "nodeC3": {
        "nodeC2": "A1",
        "nodeB3":"D1"
    },
    "nodeC4":{
        "nodeC3":"A1",
        "nodeB4":"D1"
    }
}

def transfer_st(current_node_id, source_node_id):
    if current_node_id in macroGraph.nodes() and source_node_id in macroGraph.nodes():
        if source_node_id in transitions_st.get(current_node_id, {}):
            next_st=transitions_st[current_node_id][source_node_id]
            return next_st
    return None
def transfer_node(current_node_id, source_st_id):
    if current_node_id in macroGraph.nodes():
        if source_st_id in transitions_node.get(current_node_id, {}):
            next_node=transitions_node[current_node_id][source_st_id]
            return next_node
    return None

def BellmanFord(V,graph,printArr, src):

    dist = [float("Inf")] * V
    dist[src] = 0
    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w




    printArr(dist)

def add_cars_to_graph_Road(id,mone,source,id_st):
    color = {}
    d = {}
    p = {}
    #הצומת הראשונה שאני מתחילה ממנה
    s=transfer_node(source,id_st)
    time_to_travel=get_arc_weight(macroGraph,source,s)
    asyncio.sleep(time_to_travel)
    nodes_st_lists[node][transfer_st(source,s)]=mone
    for u in macroGraph.keys():
        if u != s:
            color[u] = 'white'
            d[u] = float('inf')
            p[u] = None

    p[s] = None
    d[s] = 0

    Q = deque()
    Q.append(s)
    color[s] = 'gray'

    while Q:
        u = Q.popleft()
        # להוציא מהצומת U כמה מכוניות יש בה עכשיו
        neighbors=[]
        processes=[]
        for v in macroGraph[u]:
            if color.get(v, 'white') == 'white':
                color[v] = 'gray'
                weight_u=get_arc_weight(macroGraph,u,v)

                d[v] = d[u] + weight_u
                p[v] = u
                which_st=transfer_st(u,v)
                neighbors.append(v,which_st)
                #עובר להוסיף עבור כל שכן את מספר המכוניות שנוסעות אליו
        asyncio.run(process_neighbors(Q, u, mone, neighbors))
        color[u] = 'black'




def get_arc_weight(graph, node1, node2):
    if node1 in graph and node2 in graph[node1]:
        return graph[node1][node2]
    else:
        return None


async def process_neighbor(queue, current_intersection,neighbor, weight, current_cars):
    await asyncio.sleep(weight)
    st = transfer_st(current_intersection, neighbor)
    nodes_st_lists[neighbor][st] = nodes_st_lists[neighbor][st] + current_cars
    nodes_st_lists[current_intersection][st] = nodes_st_lists[neighbor][st] - current_cars
    priority_queue_nodes[neighbor].replace(st,nodes_st_lists[neighbor][st])
    priority_queue_nodes[current_intersection].replace(st,nodes_st_lists[current_intersection][st])
    queue.append(neighbor)
    roadAxisGraph.update_priority_axis(neighbor)    #פה צריך לשלוח לעדכן את התור עדיפויות של הצירים



async def process_neighbors(queue, current_intersection, current_cars, neighbors):
    tasks = []
    for neighbor, weight in neighbors.items():
        tasks.append(process_neighbor(queue, current_intersection,neighbor, weight, current_cars))

    await asyncio.gather(*tasks)
priority_queue_nodes={}
def initialize_priority_queue_for_all_nodes():
    for node in nodes_list:
        pqRoads = heapQueue.PriorityQueue()
        memberA1C1 = heapQueue.Member("A1C1", nodes_st_lists[node]['A1'] + nodes_st_lists[node]['C1'],
                                  nodes_st_lists[node]['A1'], nodes_st_lists[node]['C1'], True)
        memberA1A2 = heapQueue.Member("A1A2", nodes_st_lists[node]['A1'] + nodes_st_lists[node]['A2'],
                                  nodes_st_lists[node]['A1'], nodes_st_lists[node]['A2'], True)
        memberB1D1 = heapQueue.Member("B1D1", nodes_st_lists[node]['B1'] + nodes_st_lists[node]['D1'],
                                  nodes_st_lists[node]['B1'], nodes_st_lists[node]['D1'], True)
        memberB1B2 = heapQueue.Member("B1B2", nodes_st_lists[node]['B1'] + nodes_st_lists[node]['B2'],
                                  nodes_st_lists[node]['B1'], nodes_st_lists[node]['B2'], True)
        memberC1C2 = heapQueue.Member("C1C2", nodes_st_lists[node]['C1'] + nodes_st_lists[node]['C2'],
                                  nodes_st_lists[node]['C1'], nodes_st_lists[node]['C2'], True)
        memberD1D2 = heapQueue.Member("D1D2", nodes_st_lists[node]['D1'] + nodes_st_lists[node]['D2'],
                                  nodes_st_lists[node]['D1'], nodes_st_lists[node]['D2'], True)
        pqRoads.push(memberA1A2)
        pqRoads.push(memberA1C1)
        pqRoads.push(memberB1B2)
        pqRoads.push(memberB1D1)
        pqRoads.push(memberC1C2)
        pqRoads.push(memberD1D2)

roadAxisQueue=[]
heapq.heappush(roadAxisQueue,(0,"ABC1"))
heapq.heappush(roadAxisQueue,(0,"ABC2"))
heapq.heappush(roadAxisQueue,(0,"ABC3"))
heapq.heappush(roadAxisQueue,(0,"ABC4"))
heapq.heappush(roadAxisQueue,(0,"A1234"))
heapq.heappush(roadAxisQueue,(0,"B1234"))
heapq.heappush(roadAxisQueue,(0,"C1234"))
roadAxisMembers=[]

