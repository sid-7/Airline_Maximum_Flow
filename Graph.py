import networkx as nx

class Graph():
    
    def make_graph(self,flights):
        graph = nx.MultiDiGraph()
        graph.add_nodes_from(['LAX', 'SFO', 'PHX', 'SEA', 'DEN', 'ATL', 'ORD', 'BOS', 'IAD', 'JFK'])
        edge_list=[]
        for rows in flights.iterrows():
            dept = rows[1]['Source']
            arr = rows[1]['Destination']
            data = {}
            data['dept'] = rows[1]['Depature']
            data['arr'] = rows[1]['Arrival']
            data['capacity'] = rows[1]['capacity']
            edge_list.append((dept, arr, data))

        for x in edge_list:
            graph.add_edge(x[0], x[1], dept=x[2]['dept'], arr=x[2]['arr'], capacity=x[2]['capacity'])
        return graph
    
    