# -*- coding: utf-8 -*-
"""
@Author: liu
@Date: 2018-05-07 20:40:47
@Last Modified by: liu
@Last Modified time: 2018-05-07 20:40:47
"""


class Node():
    def __init__(self):
        self.next = set()
        self.color = "white"


class graph(object):
    def __init__(self):
        """[summary]
        e.g.
        If there are three egdes:
        0→1, 0→2, 2→3
        then the dictionary of graph will be like this:
        Node(0).next {Node(1), Node(2)}
        Node(1).next: {Node(0)}
        Node(2).next: {Node(0), Node(3)
        Node(3).next: {Node(2)}
        """
        self.nodes = {}

    def add_edge(self, start, end):
        """[summary]
        Add an edge into the graph

        Arguments:
            start {int} -- start node number of the edge
            end {int} -- end node number of the edge
        """
        nodes = self.nodes
        # {start node number: end node}
        if nodes.get(start):
            nodes[start].next.add(end)
        else:
            nodes[start] = Node()
            nodes[start].next = set([end])
        # {end node number: start node}
        if nodes.get(end):
            nodes[end].next.add(start)
        else:
            nodes[end] = Node()
            nodes[end].next = set([start])

    def reset_color(self):
        """[summary]
        Reset the colors of all nodes
        """
        for node in self.nodes.values():
            node.color = "white"

    def bfs(self, start, target):
        """[summary]
        Search the nearest path from start to target
        Arguments:
            start {int} -- start node number
            target {int} -- target node number

        Returns:
            list -- the nearest path from start to target
        """
        nodes = self.nodes
        # Terminate earlier
        if start not in nodes or target not in nodes:
            return None
        # Record paths, 2D list
        que = [[start]]
        # Search the graph
        while que:
            # Visit the child nodes of the first node in the que
            current_node_num = que[0][-1]
            child_node_nums = nodes[current_node_num].next
            for child_node_num in child_node_nums:
                # Append them together if the child node's not explored
                if nodes[child_node_num].color == "white":
                    que.append(que[0] + [child_node_num])
                # Target found
                if child_node_num == target:
                    self.reset_color()
                    return que[-1]
            # Pop first node in the que and marked as explored
            nodes[current_node_num].color = "black"
            que.pop(0)
        # Not found
        self.reset_color()
        return None

    def dfs(self, start, target):
        """[summary]
        Search the one path from start to target
        Arguments:
            start {int} -- start node number
            target {int} -- target node number

        Returns:
            list -- one path from start to target
        """
        nodes = self.nodes
        # Terminate earlier
        if start not in nodes or target not in nodes:
            return None
        # Record paths, 1D list
        stack = [start]
        nodes[start].color = "gray"
        # Search the graph
        while stack:
            # Visit the child node of the last node in the stack
            current_node_num = stack[-1]
            # get its child
            child_node_nums = nodes[current_node_num].next
            # set up a flag to check if there is any while child
            has_while_child = False
            for child_node_num in child_node_nums:
                # Append while child to path
                if nodes[child_node_num].color == "white":
                    has_while_child = True
                    stack.append(child_node_num)
                    # Mark child node as explored
                    nodes[child_node_num].color = "gray"
                    break
            # Mark current node as fully explored
            if not has_while_child:
                nodes[child_node_num].color == "black"
                stack.pop()
            # Target found
            if child_node_num == target:
                self.reset_color()
                return stack
        # Not found
        self.reset_color()
        return None


if __name__ == '__main__':
    # Build graph
    edges = [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5],
        [5, 6],
        [0, 7],
        [2, 7],
        [6, 9],
        [7, 8],
        [8, 9],
        [7, 10],
        [8, 11],
        [9, 11],
        [10, 13],
        [11, 13],
        [13, 14],
        [13, 17],
        [12, 15],
        [15, 16],
        [16, 17],
        [17, 18],
        [18, 19],
    ]
    rome_graph = graph()
    for edge in edges:
        rome_graph.add_edge(*edge)
    # Search path
    start, target = 2, 13
    print("The bfs path from {start} to {target} is:".format(
        start=start, target=target), rome_graph.bfs(start, target))

    print("The dfs path from {start} to {target} is:".format(
        start=start, target=target), rome_graph.dfs(start, target))
