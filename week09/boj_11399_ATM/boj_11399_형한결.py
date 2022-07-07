N = int(input())
P_list = list(map(int,input().split()))
P_list = sorted(P_list)
P_cumsum = []
P_cumsum.append(P_list[0])
for i in range(1,len(P_list)):
    P_cumsum.append(P_list[i] + P_cumsum[i-1] )
print(sum(P_cumsum))