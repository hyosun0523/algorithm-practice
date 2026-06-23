def arrinput():
    arr = list(map(int,input('값 입력:').split()))
    return arr

def ssort(arr):
    for i in range(0, len(arr)-1):
        key = i
        for j in range(i+1, len(arr)):
            if(arr[key]>arr[j]):
                key = j
        arr[i], arr[key] = arr[key], arr[i]
    print(arr)
        
def isort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while(j >= 0 and key<arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)

def bsort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr) - i - 1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

arrA = arrinput()
ssort(arrA)
arrB = arrinput()
isort(arrB)
arrC = arrinput()
bsort(arrC)
