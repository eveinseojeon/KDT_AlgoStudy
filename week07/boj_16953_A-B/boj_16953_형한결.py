import sys
N,M = sys.stdin.readline().split()
cnt = 1
while int(N)!=int(M):
    if M[-1]=='1':
        M=M[:-1]
        cnt=cnt+1
    elif int(M)%2 != 0  or int(M)<int(N):
        cnt = -1
        break
    else:
        M=str(round(int(M)/2))
        cnt=cnt+1
print(cnt)