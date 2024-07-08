from graphtheory import *

def printPath(path):
    """pathはNodeオブジェクトからなるリストとする"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result
    
def DFS(graph, start, end, path, shortest, toPrint=False):
    """graphとDigraphオブジェクト、startとendはNodeオブジェクト
    pathとshortestは、Nodeオブジェクトのリストとする
    graphでの、startノードからendノードへの最短経路を返す"""
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #サイクルを避ける
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
    return shortest

def shortestPath(graph, start, end, toPrint=False):
    """graphはDigraphオブジェクト、startとendはNodeオブジェクトとする
    graphでのstartノードからendノードへの最短経路を返す"""
    return DFS(graph, start, end, [], None, toPrint)