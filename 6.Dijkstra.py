# -*- coding: UTF-8 -*-
# 狄克斯特拉算法

graph = {}

# 创建起点及其花销
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# 节点 a 的边及其花销
graph["a"] = {}
graph["a"]["fin"] = 1

# 节点 b 的边及其花销
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

# 终点
graph["fin"] = {}

# 开销表
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 存储父节点表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 记录已处理的节点
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print parents
