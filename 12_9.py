from graphtheory import *

def BFS(graph, start, end, toPrint=False):
    """graphはDigraphオブジェクト、startとendはNodeオブジェクトとする
    graphでの、startノードからendノードへの最短路を返す"""
    initPath=[start]
    pathQueue=[initPath]
    while len(pathQueue) != 0:
        #pathQueueの中の一番古い要素を参照し、それを取り除く
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None
    