#!/usr/bin/env python
# -*- coding: utf-8 -*-
start = "hit"
end = "cog"
a_list = ["hit", "hot", "dot", "dog", "lot", "log", "cog"]
a_dict = {}
def find_path(path):
    length = len(path)
    node = path[length-1]
    # 如果节点为终点就返回
    if node == end:
        print(path,"该路径可以从",start,"到",end)
        return
    choices = []
    # 将只相差一个字母但不在path中的单词加入choices
    for choice in a_dict[node]:
        if choice not in path:
            choices.append(choice)
    # 如果长度为0就代表已经无法在替换下去
    if len(choices) == 0:
        print(path,"该路径无法再次替换单词")
        return
    for a_choice in choices:
        a_path = path.copy()
        a_path.append(a_choice)
        # print(a_path)
        find_path(a_path)

if __name__ == "__main__":
    path = []
    path.append("hit")
    for i in a_list:
        a_dict[i] = []
    # 找到和该单词只相差一个字母的所有单词。
    for i in range(len(a_list)):
        for j in range(len(a_list)):
            sum = 0
            for k in range(3):
                if (a_list[i][k] == a_list[j][k]):
                    sum += 1
            if sum == 2:
                a_dict[a_list[i]].append(a_list[j])
    print("单词只相差一个字母的表")
    for key in a_dict.keys():
        print("单词",key)
        print("只相差一个字母的单词",a_dict.get(key))
    print("以下为所有路径")
    find_path(path)

