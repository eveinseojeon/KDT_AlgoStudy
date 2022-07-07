import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
do = [] # 도화지, 그래프
cnt = 0 # 그림의 갯수 변수
res = [0] # 그림의 넓이 담을 배열

# 그림 그리기
for i in range(n):
    do.append(list(map(int,input().rstrip().split())))
    
def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append([x,y])
    do[x][y] = 0 # 시작점 방문처리
    are = 1 # 넓이는 1부터 시작
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and do[nx][ny] == 1:
                are += 1 # 넓이 키우기
                do[nx][ny] = 0 # 방문 처리            
                queue.append([nx, ny]) # 큐에 삽입
    res.append(are) # 그림의 넓이 배열에 삽입

for x in range(n):
    for y in range(m):
        if do[x][y] == 1: # 그림이 그려져있다면 BFS 탐색 시작
            bfs(x,y)
            cnt += 1 # 그림 갯수 +1

print(cnt) # 그림갯수 출력
print(max(res)) # 그림의 넓이 최대값 출력