def summation(arr):
    arr = list(map(int, arr.split()))
    maxim = -10000
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i] = arr[i]*(-1)*2
        if arr[i] > maxim:
            maxim = arr[i]
    c = list(map(lambda x: x/maxim, arr))
    return sum(c)
print(summation(input()))
