N = int(input()) # N: 묘목 구입 개수

trees = list(map(int,input().split())) #각 나무가 자라는 시간 리스트

trees = sorted(trees,reverse=True) # 내림차순 정렬

day_tree = []
for i in range(0,N):
    day_tree.append(trees[i] - N + i+1) #정렬된 나무가 각자 걸리는 시간을 리스트에 담음

print(max(day_tree) + N +1)
# 정렬했을때 최대 자라는 날 + 나무를 심는데 걸리는날  + 다음날 초대(1)