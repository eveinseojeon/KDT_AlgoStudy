N,L = map(int,input().split())
pipe = list(map(int,input().split()))
pipe.sort()

start = 0
cnt = 0
for i in pipe:
    if start<i:
        start = i+L -1
        cnt = cnt + 1
print(cnt)        