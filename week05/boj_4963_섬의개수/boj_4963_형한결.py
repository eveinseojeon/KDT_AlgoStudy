#import sys
#input = sys.stdin.readline

dire=[(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)] # 8 방향

def  traverse(matrix,i,j):
    if matrix[i][j]==0:
        return #바다는 아무것도 리턴하지 않는다.
    
    matrix[i][j] = 0 #방문한곳은 0으로 처리하여 다시 섬으로 가는 것을 방지
    
    for d in dire: #현재 위치에서 갈 수 있는 범위
        ny = i + d[0]
        nx = j + d[1]
        if nx <0 or ny < 0 or nx >= x or ny >= y:
            continue #다시 for문으로 돌아가 다음 방향 탐색
        if matrix[ny][nx]==1:
            traverse(matrix,ny,nx)


def countIsland(x,y,matrix):
    count = 0
    for i in range(y):
        for j in range(x):
            if matrix[i][j]==1:
                count +=1
                traverse(matrix,i,j)


while True:
    x,y = map(int,input().split())
    if x==0 and y==0:
        break
    matrix = [list(map(int,input().split()))for _ in range(y)]
    
    print(countIsland(x,y,matrix))