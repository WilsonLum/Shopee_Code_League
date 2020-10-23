# T = case number
# 
while True:
    try:
        T = int(input('Case : '))
    except ValueError:
        print("Not an integer! Please enter an integer.")
        continue
    else:
        break

for i in range(T):
    N=list(map(int,input().split(' ')))
    
    if i == 0:
        data = [ [0] * N[0] for _ in range(T)]
        Q    = [ [0] * N[1] for _ in range(T)]
        
    for j in range(N[0]):
        data[i][j] = (input())
        
    for k in range(N[1]):
        Q[i][k] = (input())

for a in range(len(Q)):
    print("Case ", a+1, ":\n")
    for b in range(len(Q[a])):
        count = 0
        for c in range(len(data[a])):
            if Q[a][b] == 0:
                break
            if Q[a][b] in data[a][c]:
                count+=1
        print(count)
            