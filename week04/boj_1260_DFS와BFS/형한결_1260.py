N,M,start = map(int,input().split())

graph_dict = {}
for i in range(1,1001):
    graph_dict[i]=[]
#1부터 1000을 키를 가지고 각 키값은 키와 연결되어있는 숫자 표시할 빈 리스트

for _ in range(0,M): #간선의 개수 만큼 딕셔너리에 넣어준다.
    a = list(map(int,input().split())) #정점과 간선의 정보가 간선의 개수만큼 입력된다.
    for i in range(1,N+1): #정점들이 순서대로 들어간다.
        if a[0]==i: #만약 입력된 값(a)이 i 로 시작한다면
            graph_dict[i].append(a[1]) #i의 키값은 입력된 값(a)의 두번째 값이된다.
            graph_dict[i] = sorted(graph_dict[i])  # 작은것부터 탐색하니 정렬해준다.
            graph_dict[a[1]].append(i) # 양방향 간선일경우
            graph_dict[a[1]] = sorted(graph_dict[a[1]]) # 양방향으로 입력한 리스트 정렬
            break # 키값을 update했으니 끊고  다시 a를 받는다

def r_dfs(start,discover=[]): #시작점 start, 방문한것은 discover
    discover.append(start) # 시작점은 방문한것에 넣어주고
    for i in graph_dict[start]: # 시작점에 키값 중 작은것 부터 탐색한다, 만약 탐색할것이 없으면 이전 탐색한 것중에 그 다음 숫자를 고른다.
        if i not in discover:
            discover = r_dfs(i,discover)
    return discover

print(*(r_dfs(start)))


from collections import deque

def bfs(start,discover=[],s_deq=deque([])): #discover : 방문한곳 , s_deq : 시작 후보점
    discover.append(start) #스타트점을 방문처리하고
    s_deq.append(start) # 시작 후보점을 만들어준다
    while s_deq: #시작 후보점이 빌때까지
        s = s_deq.popleft() #시작 후보를 뽑아서
        for i in graph_dict[s]: #시작 후보노드를 탐색
            if i not in discover: #방문하지 않았으면
               discover.append(i) #방문처리 해주고
               s_deq.append(i) #시작후보순위에 올려둔다.
    return discover

print(*(bfs(start)))