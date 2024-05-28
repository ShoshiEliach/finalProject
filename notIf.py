import networkx as nx
def A1(id):
    return id =="A1"
def C1(id):
    return id =="C1"
def A1OrC1(id):
    return id =="A1" or id =="C1"
def check():
    A1('ff') and func()
def func():
    print('ffffffff')
check()


def find_source_nodes(graph):
    source_nodes = [node for node in graph.nodes if graph.in_degree(node) == 0]
    return source_nodes
