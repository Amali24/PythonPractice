def mean(ar, n):
    n = int(n)
    total = 0
    for num in ar:
        num = int(num)
        total += num   
    return total / n

def median(ar, n):
    n = int(n)
    if n % 2 == 0:
        return int(ar[n//2]) + int(ar[(n//2) + 1]) / 2
    else:
        return int(ar[n//2])

def mode(ar, n):
    nums = {}
    for num in ar:
        if num in nums:
            nums[int(num)] += 1
        else:
            nums[int(num)] = 1
    return max(nums.values())

if __name__ == '__main__':
    n = input()
    ar = []
    ar = input().split()

    meanout = mean(ar,n)
    print(str(meanout))

    medianout = median(ar,n)
    print(str(medianout))

    modeout = mode(ar,n)
    print(str(modeout))