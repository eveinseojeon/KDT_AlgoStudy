n= int(input())
dp = [0 for _ in range(n)]
seq = list(map(int,input().split()))
dp[0]=seq[0]
for i in range(len(seq)-1):
    if dp[i]>0:
        dp[i+1] = dp[i]+seq[i+1]
    else: 
        dp[i+1]=seq[i+1]

print(max(dp))