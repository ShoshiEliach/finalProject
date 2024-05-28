import networkx as nx

def create_subgraphs_with_two_nodes(graph):
    subgraphs = {}
    # Get the first source node in the graph

    first_source = next(iter(graph.nodes), None)
    if first_source:
        successors = list(graph.successors(first_source))

        for child_node in successors:
            subgraph = graph.subgraph([first_source, child_node])
            last_node_name = list(subgraph.nodes)[-1]
            subgraphs[last_node_name] = subgraph
            #מחזיר את 2 הצירים הראשונים
        return subgraphs
def check_fatherNode_to_grandchildren(checks):
    #רשימת הצמתים שמתחברות לציר של אבא שלהם
    connect_son_to_father_axis=[]
    #רשימת הצמתים שפותחות ציר חדש
    new_axis=[]
    for check in checks:
        G=check[0]
        father=check[1]
        son=check[2]
        grandchildren_list=check[3]
        for grandchild in grandchildren_list:
            int_grandchild=int(grandchild)
            print('father',father,'son',son,'grandchild',int_grandchild)
            if nx.has_path(G, father, int_grandchild):
                new_axis.append((son, grandchild))

            else:
                connect_son_to_father_axis.append(( father,son, grandchild))
    return connect_son_to_father_axis,new_axis