#N = int(input())
#if N % 2 == 0:
#    print("CY")
#else:
#    print("SK")

#DP 풀이
N = int(input())
dp=[0 for _ in range(N+1)]
dp[1] = 'W'
dp[2] = 'L'
dp[3] = 'W'
for i in range(4,N+1):
    if dp[i-1] == 'L' or dp[i-3] == 'L':
        dp[i] = 'W'
        
if dp[N] =='W':
    print('SK')
else:
    print('CY')    