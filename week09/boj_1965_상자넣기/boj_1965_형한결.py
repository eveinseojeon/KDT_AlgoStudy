n = int(input())
box = list(map(int,input().split())
dp = [ 0 for _ in range(n)]
for i in range(n-2,-1,-1):
    max_list = []
    for j in range(n-1,i,-1):
        if box[i] < box[j]:
            max_list.append(dp[j])
        dp[i] = max(max_list)
print(max(dp))