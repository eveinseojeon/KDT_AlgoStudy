rope =[]
N = int(input())
for i in range(0,N):
    WT = int(input())
    rope.append(WT)
rope = sorted(rope,reverse=False) # 중량은 제일 약한 로프에게 달려있다.


find_WT = []
for i in range(0,len(rope)):
    find_WT.append(rope[i]*(N-i))  # 로프 조합으로 중량을 들 수 있는 모든 경우의 수

print(max(find_WT))