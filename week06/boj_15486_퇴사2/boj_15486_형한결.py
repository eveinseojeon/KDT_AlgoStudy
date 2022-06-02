import sys

n = int(sys.stdin.readline().rstrip())
t = []
p = []
for _ in range(n):
    small_t, small_p = map(int, sys.stdin.readline().rstrip().split())
    t.append(small_t)
    p.append(small_p)

dp = [0 for _ in range(n+1)]
local_max = dp[0]

for i in range(n):
    local_max = max(local_max, dp[i])
    # i번까지 얻을 수 있는 dp 중 최댓값 local_max

    last_idx = t[i] + i
    # i번 상담을 할 경우 last_idx날까지 상담해야 한다.
    if last_idx > n: continue
    # 상담 자체를 하지 못하는 경우
    dp[last_idx] = max(local_max + p[i], dp[last_idx])
    # last_idx 날까지 i번 상담을 한다면 p[i]를 더한 값으로 갱신
    # 상담을 하지 않는 이득이 더 크다면 그대로.

print(max(dp))
# 모든 상담 가능한 dp에서 얻을 수 있는 가장 큰 이득