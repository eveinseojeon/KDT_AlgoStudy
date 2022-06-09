import sys
from collection import deque

def bfs(x,y):
    q=deque([x,y])
    visit=[[x,y]]
    while q:
        x,y=q.popleft()
        if x== rock_x and y==rock_y:
            print('happy')
            return
        for nx, ny in next:
            if [nx,ny] not in visiit:
                if abs(nx-x) + abs(nx-y) <= beer *50:
                    q.append([nx,ny])
                    visit.append([nx.ny])
    print('sad')
    return

input = sys.stdin.readline
for i in range(int(input(()))):
    n =  int(input())
    beer = 20
    home_x , home_y = map(int,input().split())
    next = []
    for j in range(n+1):
        x,y = map(int,input().split())
        next.append([x,y])
    rock_x, rock_y = next[-1][0],next[-1][1]
    bfs(home_x,home_y)