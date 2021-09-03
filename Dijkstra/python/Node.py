class Node:

    def __init__(self, node_name, connections=None):
        """
        Initializes the Node with a name an an array of connections
        :param node_name: String
        :param connections: List
        """
        self.connections = connections if connections else []
        self.node_name = node_name
        return

    def add_connection(self, node, nodal_distance):
        """
        Adds a connection to the specified node and the node itself with the weight / nodal distance
        :param node: Node
        :param nodal_distance: Integer
        :return: None
        """
        self.connections.append((node, nodal_distance))
        node.connections.append((self, nodal_distance))
        return

    def get_connection(self):
        """
        Gets all the connections for a given node in a clean, formatted way
        Formatted as
        {
            Node: Distance
        }
        :return: dict()
        """
        conn_list = {}
        for i in self.connections:
            conn_list[i[0]] = i[1]
        return conn_list

