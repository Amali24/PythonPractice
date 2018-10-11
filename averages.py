def mean(ar, n):
    total = 0
    for num in ar:
        num = num
        total += num   
    return total / n

def median(ar, n):
    ar.sort()
    if n % 2 == 0:
        return ar[n//2] + ar[(n//2) + 1] / 2
    else:
        return ar[n//2]

def mode(ar, n):
    nums = {}
    for num in ar:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1
    key = max(nums, key = nums.get)
    return key

if __name__ == '__main__':
    n = int(input())
    arin = []
    arin = input().split()
    ar = []
    for num in arin:
        ar.append(int(num))

    meanout = mean(ar,n)
    print(str(meanout))

    medianout = median(ar,n)
    print(str(medianout))

    modeout = mode(ar,n)
    print(str(modeout))