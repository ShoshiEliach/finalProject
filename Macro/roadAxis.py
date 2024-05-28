import ctypes
import heapq
import string

import hash
from datetime import time
import func
import networkx as nx
import stack
import myQueue
import pandas as pd

class RoadAxisManager:


    def __init__(self,G):
        self.roadAxisQueue = []
        self.roadGraph=G
        self.graphs_axis={}
    #פונקציה שמפרקת לצירים מהגרף
    def init_from_graph(self):
        G=self.roadGraph
        nodes=G.nodes()
        edges=G.edges()
        # עובר על כל צומת בגרף בשביל לקבל את פרטי הצומת
        details_for_node={}
        for node in G.nodes:
            node_name = G.nodes[node]
            node_key = str(node_name)
            details_for_node[node_key] = {'axis': 0}
        #source_node=notIf.find_source_nodes(G)
        # מוצא את צומת המקור בגרף ויוצר ממנה תתי גרפים לפי מספר הבנים שלה
        graphs_axis=func.create_subgraphs_with_two_nodes(G)

        #
        queue_father= myQueue.Queue()
        stack_sons= stack.Stack()
        father = next(iter(G.nodes), None)
        queue_father.enqueue(father)
        for i,graph in graphs_axis.items():
            #לוקח את הצומת האחרונה בגרף
            son=list(graph.nodes())[-1]
            #int_father=int(father)
            stack_sons.push(son)

            #יוצר תת גרף רק עם הבנים הישירים של father

            #כל שאר הצמתים בגרף נמצאים בsons
            checks=[]

        while stack_sons and queue_father:
            father=queue_father.peek()

            #print('father',father)

            #stack_sons.print_stack_order()

            #for son in sons:
            son=stack_sons.pop()
            # כל הצמתים שהם בנים ישירים של son
            grandchildrens = list(G.successors(son))
            if not grandchildrens:
                break
            # father_graph = nx.ego_graph(G, son)
            # שמים בcheck גרף את הגרף המקורי ללא צומת הson
            check_graph = G.copy()
            int_son = int(son)
            check_graph.remove_node(int_son)
            # checks זה הרשימה שצריך לעשות עליה את כל הבדיקות לכל הצמתים על הצירים
            checks.append((check_graph, father, int_son, grandchildrens))
            if stack_sons.is_empty() and queue_father.peek():
                queue_father.dequeue()
                queue_father.insert_sons(G,father)

                stack_sons.insert_sons(G,queue_father.peek())
            '''if len(list(G.predecessors(first_node))) == 1:
                print('hhhhh')
                sons.append(G.successors(first_node))
                print(sons)'''


        connect_son_to_father_axis, new_axis=func.check_fatherNode_to_grandchildren(checks)
        connect_check=[tuple_[1:] for tuple_ in connect_son_to_father_axis]

        hash_connect= hash.HashTableOfLists(len(connect_check))
        for i in connect_check:
            hash_connect.insert(i,(i[0],i[1]))
        remove_list=[]
        for i in new_axis:
            find=hash_connect.search(i)
            if find:
                remove_list.append(i)
        new_axis = [item for item in new_axis if item not in remove_list]

        reversed_connections = [tuple(reversed(connection)) for connection in connect_son_to_father_axis]
        #print('reversed_connections',reversed_connections)
        for c in reversed_connections:connect_son_to_father_axis.append(c)
        #print('connect',connect_son_to_father_axis)
        #print('new',new_axis)
        #print('remove',remove_list)
        # #לחבר את הנתונים לכל הצירים
        #
        # for new in new_axis:
        #     new_graph_axis = G.subgraph(new).copy()
        #     new_graph_axis.add_edges_from(
        #         (u, v, G[u][v]) for (u, v) in new_graph_axis.edges if u in new and v in new)
        #     #graphs_axis.append(new_graph_axis)

        idsAxis = string.ascii_uppercase[:len(connect_son_to_father_axis)]
        for i in range(len(connect_son_to_father_axis)):
            self.graphs_axis[idsAxis[i]] = connect_son_to_father_axis[i]
        print('graphs_axis',self.graphs_axis)


    def build_queue_axis(self,graphs_axis):
        for graph,i in graphs_axis.values():
            axis_name="axis"+i
            axis_priority=0
            #לבנות תור עדיפויות של צירים

            for node in graph:
                node.axis=axis_name
                axis_priority=axis_priority+node.priority
            heapq.heappush(self.roadAxisQueue, (axis_priority, axis_name))
            heapq.heapify(self.roadAxisQueue)

            #######################

            self.add_axis_to_queue(axis_name)
    def add_axis_to_queue(self, axis_name):
        heapq.heappush(self.roadAxisQueue, (0, axis_name))

    # def update_path_for_node(self, node, paths):
    #     self.nodes_st_lists[node] = paths
    #
    # def update_path_for_axis(self, axis_name, node, updated_path):
    #     for axis, paths in self.nodes_st_lists.items():
    #         if axis.startswith(axis_name):
    #             for i, (path, weight) in enumerate(paths):
    #                 if path == node:
    #                     self.nodes_st_lists[axis][i] = (node, updated_path)

    def change_priority_by_axis_name(self, axis_name,value):
        for priority, name in self.roadAxisQueue:
            if name == axis_name:
                priority=priority+value
    def update_priority_axis(self,node):
        self.change_priority_by_axis_name(node.axis,node.priority)
        heapq.heapify(self.roadAxisQueue)
    #
    # למצוא את הציר לפי הצומת והנתיב
    def find_axis_by_node(self,id_node,id_st):
        for graph in self.graphs_axis:
            if id_node in graph.nodes():
                father=list(graph.nodes())[-1]
                num1=father.name[-1]
                num2=id_node[-1]
                if num1==num2 and id_st[0]=='C' or num1-num2==1 and id_st[0]=='B':
                #צריך לבדוק לפי שם הנתיב
                    axis=graph
        return axis




    def green_wave(self,id_node_path):
        id_node=id_node_path[:6]
        id_path=id_node_path[6:]
        #פה צריך למצוא את הציר לפי הצומת והנתיב
        graph_axis=self.find_axis_by_node(id_node,id_path)
        for neighbor in graph_axis[id_node]:
            time.sleep(self.roadGraph[id_node][neighbor])
            neighbor.priority=neighbor.priority+10
            #לעדכן את הציר
            node=neighbor








    #לבנות תור עדיפויות של צירים
#לעשות פעולה שמעדכנת את התור שמקהלת שם של צומת ובודקת לאיזה ציר היא שייכת
def convert_edges(edges):
    converted_edges = []
    for edge in edges:
        if len(edge) >= 3 and isinstance(edge[2], dict) and 'weight' in edge[2]:
            source = edge[0]
            destination = edge[1]
            weight = edge[2]['weight']
            converted_edges.append((source, destination, weight))

    return converted_edges



def axisGraph():
    #print('e')
    graphRoads=nx.DiGraph()
    #print('hello')
    #print('hello')
#nodes=[1,2,3,4,5,6,7,8,9]
#edges=[(1,2,{'weight': 7}),(2,3,{'weight': 3}),(1,4,{'weight': 9}),(4,7,{'weight': 10}),(2,5,{'weight': 5}),(5,8,{'weight': 8}),(3,6,{'weight': 3}),(6,9,{'weight': 5}),(4,5,{'weight': 7}),(5,6,{'weight': 2}),(7,8,{'weight': 4}),(8,9,{'weight': 6})]

#g_try.add_nodes_from(nodes)
#g_try.add_edges_from(edges)
    df = pd.read_excel("C:\\Users\\User\\Documents\\finalProject\\graph_excel.xlsx")
    for index, row in df.iterrows():
        node1 = row['Node1']
        node2 = row['Node2']
        weight = row['Weight']
        graphRoads.add_edge(node1, node2, weight=weight)

# Print the edges to verify if they are correctly read
    #print(graphRoads.edges(data=True))
    try_axis=RoadAxisManager(graphRoads)
    try_axis.init_from_graph()


    edges_cpp=convert_edges(graphRoads.edges)

    data_size=len(try_axis.graphs_axis)
    graph_data = (ctypes.c_char * data_size)()
    graph_data_values = (ctypes.c_int * (data_size * 3))()
    print(try_axis.graphs_axis)
    with open('graphs_axis.txt', 'w') as file:
        for key, value in try_axis.graphs_axis.items():
            file.write(f"{key}: {value}\n")
    with open('data.txt', 'w') as file:
        for key, values in try_axis.graphs_axis.items():
            file.write(f"{key} {values[0]} {values[1]} {values[2]}\n")

    lib = ctypes.CDLL("C:\\Users\\User\\Documents\\finalProject\\try\\try\\functions.so")

    libMain=ctypes.CDLL("C:\\Users\\User\\Documents\\finalProject\\try\\try\\try.so")
    flat_edges = [val for edge in edges_cpp for val in edge]

# Convert the nodes and flat_edges to ctypes arrays
    nodes_arr = (ctypes.c_int * len(graphRoads.nodes))(*graphRoads.nodes)
    edges_arr = (ctypes.c_int * len(flat_edges))(*flat_edges)

    #lib.parseAndPrint(edges_arr, len(flat_edges))
    #lib.process_graph_data.restype = None
    #lib.process_graph_data.argtypes = [POINTER(ctypes.c_char), POINTER(c_int), c_int]


    print("graph_data_value",graph_data_values)
    print("d_g",graph_data)
    print("data_size",data_size)
    return graph_data_values

axisGraph()
#lib.process_graph_data(graph_data, graph_data_values, data_size)

#if __name__ == "__main__":
    #main()

#print(adj_list)

#father_graph = nx.ego_graph(g_try, '1')

#print(father_graph)
