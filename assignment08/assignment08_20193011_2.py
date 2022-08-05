## 최단 경로 찾기

## Dijksra 알고리즘

#최소 dist 정점을 찾는 함수 
INF = 10000
def choose_vertex(dist, found):
    min = INF
    minpos = -1
    for i in range(len(dist)):                    
        if dist[i]<min and found[i] == False :    
            min = dist[i]
            minpos = i
    return minpos;                                # 최소 dist 정점의 인덱스 변환

# start에서부터 다른 모든 정점까지의 최단 경로 계산

def shortest_path(vtx, adj, start):
    vsize = len(vtx)                             
    dist = list(adj[start])                      
    path = [start]*vsize                         
    found = [False]*vsize                        
    found[start] = True                          
    dist[start] = 0                              
    
    for i in range(vsize):             
        u = choose_vertex(dist, found)           
        found[u] = True                          
        
        for w in range(vsize) :                  
            if not found[w]:                     
                if dist[u] + adj[u][w] < dist[w]: 
                    dist[w] = dist[u] + adj[u][w] 
                    path[w] = u                   
                    
    return path, dist   

# 데이터 생성
vertex = [0,1,2,3,4,5,6]
weight = [[0, 4, 8, INF, INF, INF, 10],
         [4, 0, 2, 5, 11, INF, INF],
         [8, 2, 0, INF, 9, 4, 5],
         [INF, 5, INF, 0, 7, INF, INF],
         [INF, 11, 9, 7, 0, 2, 8],
         [INF, INF, 4, INF, 2, 0, INF],
         [10, INF, 5, INF, 8, INF, 0]]    

# 최단 경로 탐색 
while 1:
    start = int(input("시작점? "))
    end = int(input("도착점? "))

    path, dist = shortest_path(vertex, weight, start)

    e = end
    p = [] 
    p.append(vertex[e])
    while (path[e] != start):
        p.append(vertex[path[e]])
        e = path[e]
    p.append(vertex[path[e]])


    print("경로는 ", end = '')
    print(p[len(p)-1] , end = "-")
    for i in range(len(p)-2,0 ,-1):
        print(p[i], end = "-")
    print(p[0])

    print("거리는 ", dist[end])
    print()                           
