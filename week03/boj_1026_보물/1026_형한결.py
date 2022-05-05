N= int(input())
A= list(map(int,input().split()))
B= list(map(int,input().split()))

A = sorted(A,reverse=True)
B = sorted(B,reverse=False)

sum_AB = 0
for i in range(len(A)):
    sum_AB = sum_AB + A[i]*B[i]
print(sum_AB)