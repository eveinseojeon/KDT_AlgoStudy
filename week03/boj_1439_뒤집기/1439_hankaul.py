S = input()

count_0 = 0 # '01' 카운트
count_1 = 0 # '10' 카운트

for i in range(len(S)-1):
    if S[i] != S[i+1]  and S[i]=='0': # '01'찾기
        count_0 = count_0+1
    elif S[i] != S[i+1] and S[i] =='1': #'10'찾기
        count_1 = count_1 +1


print(max(count_0,count_1))
