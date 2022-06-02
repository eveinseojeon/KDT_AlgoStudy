import sys
N = int(input())
A = list(map(int,(input().split())))

memory = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[j]>A[i]:
            memory[i]=max(memory[i],memory[j]+1)

print(max(memory))
