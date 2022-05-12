N = int(input())
L = int(input())

graph_dict = {}
for i in range(1,101):
    graph_dict[i]=[]

for _ in range(0,L):
    a = list(map(int,input().split()))
    for i in range(1,N+1):
        if i==a[0]:
            graph_dict[i].append(a[1])
            graph_dict[a[1]].append(i)
            break

for i in range(1,N+1):
    sorted(graph_dict[i])


def r_bfs(start,discover=[]):
    discover.append(start)
    for s in graph_dict[start]:
         if s not in discover:
            r_bfs(s,discover)
    return discover

print(len(r_bfs(1)[1:]))