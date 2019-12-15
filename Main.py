from Graph import Graph
from NetworkFlow import NetworkFlow
import pandas as pd

#the input is taken in the form of csv file and in a dataframe flights.
flights=pd.read_csv('flights.csv')

#creating the object of the graph class
g=Graph()

#passing the dataframe to the class-method to generate the graph
graph=g.make_graph(flights)

#creating the object for NetworkFlow class
object_nf = NetworkFlow(graph) #passing the graph to the network flow
print("Maximum Number of People that can travel from Los Angeles to New-York: " + str(object_nf.total_flow))