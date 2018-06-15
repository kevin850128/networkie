import networkx as nx
import pandas as pd

class LoadFromFile(object):
    def __init__(self):
        """
        Initiate variables for the class.
        """
        self.g = nx.Graph()
        
        pass
    def from_edgelist(self, path):
        '''
        Read graph in edgelist txt format from `path`.

        Parameters
        ----------
        path: `str`
            The path to the edgelist text file. Note that the node index must start from 0.

        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.

        '''

        edgelist = []
        with open(path, 'r') as f:
            for line in f:
                node_pair = line.replace('\n', '').split(' ')
                edgelist += [node_pair]
        self.g.add_edges_from(edgelist)
        print(nx.info(self.g))
        print('Edgelist txt data successfully loaded into a networkx Graph!')
        return self.g

    def from_in_class_network(self, path):  # This is Prob. 3-a.
        '''
        First, create a dictionary that store every id's connected node numbers.
        Then use the dictionary with for loop to create the edge list for our network.
        Finally, we can put nodes and edges into our empty network. 
        '''
        rawdata = pd.read_csv(path, delimiter = "\t")
        md={}
        for i in rawdata.index:
            if rawdata.loc[i,"IDs-of-acquaintances"]==" ":
                continue
            elif type(eval(rawdata.loc[i,"IDs-of-acquaintances"]))==tuple:
                md[rawdata.loc[i,"ID"]] = list(eval(rawdata.loc[i,"IDs-of-acquaintances"]))
            else:
                md[rawdata.loc[i,"ID"]] = [eval(rawdata.loc[i,"IDs-of-acquaintances"])]
        edge = []
        for d in md:
            for k in range(len(md[d])):
                edge.append((d,md[d][k]))
        node = list(rawdata["ID"])
        self.g.add_nodes_from(node)
        self.g.add_edges_from(edge)
        return self.g
