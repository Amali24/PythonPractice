import statistics
if __name__ == '__main__':
    n = int(input())
    xin = input().split()
    fin = input().split()
    x = []
    f = []
    s = []
    for i in range(0, n):
        x.append(int(xin[i]))
        f.append(int(fin[i]))
    
    for i in range(0, n):
        for j in range (0, f[i]):
            s.append(x[i])

    s.sort()

    size = len(s)

    if size % 2 != 0:
        L = s[0:size//2]
        U = s[size//2 + 1:]
    else: 
        L = s[0:size//2]
        U = s[size//2:]

    q1 = statistics.median(L)
    q3 = statistics.median(U)

    diff = q3 - q1

    print(str(diff))