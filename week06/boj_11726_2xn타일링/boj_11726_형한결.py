import sys
y= int(sys.stdin.readline())
memory = [0 for x in range(y+1) ]


memory[1] = 1
memory[2] = 2

for i in range(3,y+1):
    memory[i]= memory[i-1] + memory[i-2]
    
print(memory[y]%10007)