def arrinput():
    arr  = list(map(int, input('값 입력:').split()))
    return arr


def intinput():
    a = int(input('찾을 값 입력:'))
    return a

def print_result(result):
    if(result is None):
        print('값 없음')
    else:
        print(result)

def ssort(arr):
    for i in range(0, len(arr)-1):
        key = i
        for j in range(i+1,len(arr)):
            if(arr[key]>arr[j]):
                key = j
        arr[i], arr[key] = arr[key], arr[i]

def isort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while(j >= 0 and arr[j]>key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def bsort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i -1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def lsearch(arr, key):
    for i in range(0, len(arr)):
        if (arr[i] == key):
            return i
    return None

def bsearch(arr, key):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (high + low)//2
        if(arr[mid] == key):
            return mid
        elif(arr[mid]>key):
            high = mid - 1
        elif(arr[mid]<key):
            low = mid + 1
    return None
        

arrA = arrinput()
ssort(arrA)
print(arrA)

arrB = arrinput()
isort(arrB)
print(arrB)

arrC = arrinput()
bsort(arrC)
print(arrC)

intA = intinput()
indexA = lsearch(arrA, intA)
print_result(indexA)

intB = intinput()
indexB = bsearch(arrB, intB)
print_result(indexB)
