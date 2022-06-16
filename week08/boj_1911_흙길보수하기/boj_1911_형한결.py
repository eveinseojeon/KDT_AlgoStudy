from collections import deque
road=deque([])
N,L = map(int,input().split())
for i in range(N):
    s,f = map(int,input().split())
    road = road + deque([x for x in range(s,f+1)])

road = deque(set(road)) #겹쳐서 입력된 웅덩이를 풀어서 정렬
land = deque([]) #웅덩이 사이의 땅
for i in range(len(road)-1):
    if road[i+1]-road[i]>1:
        land.append((road[i],road[i+1]))      
        
water = deque() #웅덩이 
for i in range(len(land)-1):
    water.append(range(land[i][1],land[i+1][0]))
    
water.append(range(min(road),land[0][0]))
water.append(range(land[-1][1],max(road)))   


count = 0
for i in water:
    if len(i)%L==0:
        count = count + (len(i)//L)
    else:
        count = count + (len(i)//L)+1
print(count)

# 메모리초과^^