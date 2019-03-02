#!/usr/bin/env python3
# encoding: utf-8

nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
INF = 9999
Graph = {
    'A': {'A': 0, 'B': 1, 'C': 12},
    'B': {'B': 0, 'C': 9, 'D': 3},
    'C': {'C': 0, 'E': 5},
    'D': {'D': 0, 'C': 4, 'E': 13,'F':15},
    'E': {'E': 0, 'F': 4},
    'F': {'F': 0},
}

def Dijkstra(G,v0):
    """ 使用 Dijkstra 算法计算指定点 v0 到图 G 中任意点的最短路径的距离
        INF 为设定的无限远距离值
        此方法不能解决负权值边的图
    """
    book = list()#记录已经确定的数组
    minv = v0
    # 源顶点到其余各顶点的初始路程
    dis = dict((k,INF) for k in G.keys())
    dis[v0] = 0
    while len(book) < len(G):
        book.append(minv)  # 确定当期顶点的距离
        for w in G[minv]:   # 以当前点的中心向外扩散
            if dis[minv] + G[minv][w] < dis[w]: #如果从当前点扩展到某一点的距离小与已知最短距离  
                dis[w] = dis[minv] + G[minv][w] #对已知距离进行更新
        new = INF # 从剩下的未确定点中选择最小距离点作为新的扩散点
        for v in dis.keys():
            if v in book: continue
            if dis[v] <= new: #如果不加等号,会导致最后无法到达的点添加不进去list,这样while循环不会结束
                new = dis[v]
                minv = v
        print(book)
    return dis
    

if __name__ == '__main__':
    dis = Dijkstra(Graph,'B')
    print(dis)
