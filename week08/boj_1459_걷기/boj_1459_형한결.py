x,y,w,s = map(int,input().split())
# s : 대각선 w:멘하튼
if 2*w <= s: #대각선을 섞을 필요가 없는 경우
    print(x*w + y*w)

elif w>=s: #대각선만으로 가야할 경우
    if (x+y)%2==0: 
        if x>y:
            print(x*s)
        else:
            print(y*s)
    else: #홀수일때는 어쩔수없이 직선 하나 추가
        if x>y:
            print((x-1)*s+w)
        else:
            print((y-1)*s+w)   
elif x==y: #정상적인 케이스
    print(s*x)
else:
    if x<y:
        print(s*x + w*(y-x))
    else:
        print(s*y + w*(x-y))