if __name__ == '__main__':
    n = int(input())
    xin = input().split()
    win = input().split()

    x = []
    w = []
    for i in xin:
        x.append(int(i))
    for i in win:
        w.append(int(i))
    total = 0
    for i in range(0, n):
        total += x[i] * w[i]
    totalWeight = sum(w)
    wAvg = total/totalWeight
    wAvg = round(wAvg, 1)
    print(str(wAvg))