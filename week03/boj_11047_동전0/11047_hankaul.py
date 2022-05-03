N, K = map(int,input().split())
poket = []
for _ in range(0,N):
    money = int(input())
    poket.append(money)

poket = sorted(poket,reverse=True)

count_list=[]
for money in poket:
    cnt = K//money
    if cnt!=0:
        count_list.append(cnt)
        K=K-(cnt*money)
        if K==0:
            break
print(sum(count_list))



'''cnt_list=[]
cnt = 1
for m in poket:
    while True:
        if cnt*m>K:
            break
        else:
            cnt=cnt+1
    if cnt>1:
        cnt_list.append(cnt-1)
        K = K - ((cnt - 1) * m)
        cnt=1
        if K==0:
            break
print(sum(cnt_list))'''