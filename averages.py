def mean(ar, n):
    return sum(ar) / n

def median(ar, n):
    if n < 1:
        return None
    if n % 2 != 0:
        return ar[n//2]
    else:
        return sum(ar[n//2-1:n//2+1])/2.0

def mode(ar, n):
    return max(ar, key = ar.count)

if __name__ == '__main__':
    n = int(input())
    arin = []
    arin = input().split()
    ar = []
    for num in arin:
        ar.append(int(num))
    
    ar.sort()

    meanout = mean(ar,n)
    print(str(meanout))

    medianout = median(ar,n)
    print(str(medianout))

    modeout = mode(ar,n)
    print(str(modeout))