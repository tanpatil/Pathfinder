class Dijkstra:

    def __init__(self, start, end, node_list):
        """
        Initializes the Entire Network of Nodes, making pathfinding possible.
        :param start: Node
        :param end: Node
        :param node_list: List
        """
        self.start = start
        self.end = end
        self.complete_map = []
        self.priority_queue = []
        # add nodes to the priority queue first
        # I know, this isn't a real priority queue
        # the format of the pq is [Node, Distance, Path]
        for i in node_list:
            if i == self.start:
                self.priority_queue.append([i, 0, None])
            else:
                self.priority_queue.append([i, float('inf'), None])

    def get_distance(self, node):
        for i in self.priority_queue:
            if node == i[0]:
                return i[1]

    def sort_pq(self):
        self.priority_queue.sort(key=lambda elem: elem[1])
        return

    def get_path(self, node, pathobject=None):
        pathobject = pathobject if pathobject else ''
        if node == self.start:
            finstr = pathobject[-1]
            for i in range(len(pathobject)-2, -1, -1):
                finstr = finstr + "->" + pathobject[i]
            return finstr + "->" +self.end.node_name
        else:
            for i in self.priority_queue:
                if node == i[0]:
                    pathobject += i[2].node_name
                    return self.get_path(i[2], pathobject)

    def mapper(self, node=None):
        # set the node that we're mapping. assume root node if no node is passed
        node = node if node else self.start
        current_distance = self.get_distance(node)
        # loop through all the connections for the given node
        for i in range(len(node.connections)):
            # now loop through the priority queue
            for j in range(len(self.priority_queue)):
                # find the node in the priority queue by comparing
                if node.connections[i][0] not in self.complete_map and node.connections[i][0] == self.priority_queue[j][0]:
                    # that means we have found the element in the pq. now lets look at the value
                    total_distance = node.connections[i][1] + current_distance
                    if total_distance < self.priority_queue[j][1]:
                        self.priority_queue[j][1], self.priority_queue[j][2] = total_distance, node
                        # once we add the new values, let us sort this pq once more
                        self.sort_pq()
        self.complete_map.append(node)
        return

    def get_route(self):
        for i in range(len(self.priority_queue)):
            self.mapper(self.priority_queue[i][0])

        return self.get_path(self.end)
