N = int(input())

dp=[2]
if N==1:
    print('SK')
elif N==2:
    print('CY')
elif N==3:
    print('SK')
elif N==4:
    print('SK')
else:
    for i in range(5,N+1):
        if (i - 1 in dp) or (i - 3 in dp) or (i - 4 in dp):
            continue
        else:
            dp.append(i)
#if N>4:
    if N in dp:
        print('CY')
    else:
        print('SK')