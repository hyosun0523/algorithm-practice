arr = list(map(int, input('값 입력:').split()))

def isort():
    for i in range(1, len(arr)):
        a = arr[i]
        j = i-1
        while(j >= 0 and arr[j] > a):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = a

isort()
print(arr)
