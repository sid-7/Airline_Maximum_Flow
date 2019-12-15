class NetworkFlow:
    def __init__(self,graph):
        self.graph = graph
        self.total_flow=0
        self.min_capacity = 99999
        self.visited_nodes_global = []
        self.total_flow=self.calculate_capacity()

    def ffs(self, edge, deptTime, visited_nodes):
        if deptTime >= 2400:
            self.min_capacity = 0
            self.visited_nodes_global.append(edge)
            return self.min_capacity

        if edge[1] == "JFK":
            if self.min_capacity > edge[2]['capacity']:
                self.min_capacity = edge[2]['capacity']
            edge[2]['capacity'] = edge[2]['capacity'] - self.min_capacity

            if edge[2]['capacity'] == 0:
                self.visited_nodes_global.append(edge)

            return self.min_capacity

        new_neighbors = []
        neighbors = []

        for e in self.graph.edges(edge[1], data=True):
            if e[2]['dept'] >= edge[2]['arr']:
                if e not in self.visited_nodes_global:
                     if e[0] not in visited_nodes:
                        neighbors.append(e)
        new_edge = []
        for e in neighbors:
            if e[2]['capacity'] > 0:
                new_edge.append(e)

        if len(new_edge)==0:
            self.min_capacity = 0
            self.visited_nodes_global.append(edge)
            return self.min_capacity
        if self.min_capacity > edge[2]['capacity']:
            self.min_capacity = edge[2]['capacity']

        t1 = int(new_edge[0][2]['arr'])
        t2 = int(edge[2]['arr'])

        if t1<t2:
            t2 = 2400 - t2
            t1 = t2+t1
        else:
            t1= t1-t2

        deptTime = deptTime + (t1)
        visited_nodes.append(new_edge[0][0])
        self.ffs(new_edge[0], deptTime,visited_nodes)

        edge[2]['capacity'] = edge[2]['capacity'] - self.min_capacity

        if edge[2]['capacity'] == 0:
            self.visited_nodes_global.append(edge)
        return self.min_capacity


    def calculate_capacity(self):
        
        neighbors = [edge for edge in self.graph.edges("LAX", data=True)]
        i  = 0
        n = len(neighbors)
        visited_nodes_local=[]
        nodes=["LAX"]

        while(i < n):

            if neighbors[i] not in self.visited_nodes_global:

                arrival_time = int(neighbors[i][2]['arr'])
                depature_time = int(neighbors[i][2]['dept'])

                if arrival_time <depature_time:
                    depature_time = 2400 - depature_time
                    arrival_time  += depature_time
                else:
                    arrival_time -= depature_time

                visited_nodes_local=[]
                visited_nodes_local.append("LAX")

                if neighbors[i][1] not in nodes:
                    nodes.append(neighbors[i][1])
                    self.visited=[]

                temp = self.ffs(neighbors[i],arrival_time ,visited_nodes_local)
                self.total_flow += temp
                self.min_capacity = 99999

            else:
                i+=1
                
        return self.total_flow