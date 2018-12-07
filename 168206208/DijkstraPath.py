#!/usr/bin/env python
# -*- coding: utf-8 -*-
class DijkstraPath():
    def __init__(self, node_map):
        self.node_map = node_map
        self.node_length = len(node_map)
        self.used_node_list = []
        self.collected_node_dict = {}
    def __call__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self._init_dijkstra()
        return self._format_path()
    def _init_dijkstra(self):
        self.used_node_list.append(self.from_node)
        self.collected_node_dict[self.from_node] = [0, -1]
        for index1, node1 in enumerate(self.node_map[self.from_node]):
            if node1:
                self.collected_node_dict[index1] = [node1, self.from_node]
        self._foreach_dijkstra()
    def _foreach_dijkstra(self):
        if len(self.used_node_list) == self.node_length - 1:
            return
        for key in list(self.collected_node_dict.keys()):  # 遍历已有权值节点
            val = self.collected_node_dict[key]
            if key not in self.used_node_list and key != to_node:
                self.used_node_list.append(key)
            else:
                continue
            for index1, node1 in enumerate(self.node_map[key]):  # 对节点进行遍历
                # 如果节点在权值节点中并且权值大于新权值
                if node1 and index1 in self.collected_node_dict and self.collected_node_dict[index1][0] > node1 + val[0]:
                    self.collected_node_dict[index1][0] = node1 + val[0] # 更新权值
                    self.collected_node_dict[index1][1] = key
                elif node1 and index1 not in self.collected_node_dict:
                    self.collected_node_dict[index1] = [node1 + val[0], key]
        self._foreach_dijkstra()
    def _format_path(self):
        node_list = []
        temp_node = self.to_node
        node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        while self.collected_node_dict[temp_node][1] != -1:
            temp_node = self.collected_node_dict[temp_node][1]
            node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        node_list.reverse()
        return node_list

# 构建图
def set_node_map(node_map, node, node_list):
    for x, y, val in node_list:
        node_map[node.index(x)][node.index(y)] = node_map[node.index(y)][node.index(x)] =  val

# 想法：为每个单词创建一个列表， 将与该单词只相差一个字母的单词加入
# 并将每个单词与 他们的只相差一个单词的集合，一个一个组成元组，权值为1放进一个队列
# 该队列为邻接表，为该邻接表建立 无向图。
# 最后将单词的关系 用图显示出来 就构成了一个 无向图相邻的单词只相差一个字母
# 用狄克斯特拉算法算法求无向图的最短路径。
if __name__ == "__main__":

    # 对应着 0 ，1，2，3，4，5，6
    node = ["hit","hot","dot","dog","lot","log","cog"]
    a_dict = {}
    lists = []
    # 为每个点 创建 队列
    for i in node:
        a_dict[i] = []
    # 为每个单词找出只相差一个字母的单词 并加入队列
    for i in range(len(node)):
        for j in range(len(node)):
            sum = 0
            for k in range(3):
                if (node[i][k] == node[j][k]):
                    sum += 1
            if sum == 2:
                a_dict[node[i]].append(node[j])
    # 将 单词 和单词组成元组，并且权值 为1
    for key, values in a_dict.items():
        for a_value in values:
            lists.append((key, a_value, 1))
    # lists去重
    for tuple in lists:
        b_tuple = (tuple[1], tuple[0], 1)
        if b_tuple in lists:
            lists.remove(b_tuple)
    node_list = lists
    node_map = [[0 for val in range(len(node))] for val in range(len(node))]
    set_node_map(node_map, node, node_list)
    # A -->; D
    # 起点
    from_node = node.index('hit')
    # 终点
    to_node = node.index('cog')
    dijkstrapath = DijkstraPath(node_map)
    path = dijkstrapath(from_node, to_node)
    # path的一个元组第一个元素为点，第二个元素为用时
    for dot in path:
        print ("单词",node[dot[0]]);