graph = {}
N,M = map(int,input().split())

#그래프 생성
for i in range(1,N+1):
    graph[i] = deque()   
for _ in range(M):
    A,B = map(int,input().split())
    graph[B].append(A)


#DFS
result = deque()
for i in range(1,N+1):
    def DFS(start,discovered=deque()):
        discovered.append(start)
        for i in graph[start]:
            if i not in discovered:
                #count+=1
                DFS(i,discovered)
        return discovered
    result.append(DFS(i))

#max 값 찾기    
len_result = deque()
for i in result:
    len_result.append(len(i))
max_result = max(len_result)

#max인 값의 컴퓨터 번호 출력
cum=deque()
for i,res in enumerate(result):
    if len(res)==max_result:
        cum.append(result[i][0])    
        
#출력        
for i in sorted(cum):
    print(i,end=' ')        
    

#^^런타임오류