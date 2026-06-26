def arr_input():
    arr = list(map(int, input('값 입력:').split()))
    return arr

def value_input():
    n = int(input('수 입력:'))
    return n

def result_print(result):
    if result is None:
        print('찾는 값이 없습니다!')
    else:
        print(result)

def selection_sort(arr):
    for i in range (len(arr)-1):
        min_ind = i
        for j in range (i+1, len(arr)):
            if arr[min_ind] > arr[j]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]

def insertion_sort(arr):
    for i in range (1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0) and (key < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def bubble_sort(arr):
    for i in range (len(arr)-1):
        for j in range (len(arr) - i - 1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def linear_search(arr, target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return None

def binary_search(arr, target):
    high = len(arr) - 1
    low = 0
    while high >= low:
        mid = (high + low)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid-1
        else:
            low = mid + 1
    return None

def fibo(n):
    if n <= 0:
        return None
    elif (n==1) or (n==2):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def hanoi(n, start, temp, end):
    if n == 1:
        print('board', 1, "->", end)
        print('총 횟수: ', 1)
    else:     
        hanoi(n-1, start, end, temp)
        print('board', n, "->", end)
        hanoi(n-1, temp, start, end)

arrA = arr_input()
selection_sort(arrA)
print(arrA)

arrB = arr_input()
insertion_sort(arrB)
print(arrB)

arrC = arr_input()
bubble_sort(arrC)
print(arrC)

intA = value_input()
indexA = linear_search(arrA, intA)
result_print(indexA)

intB = value_input()
indexB = binary_search(arrB, intB)
result_print(indexB)

print(fibo(intA))

hanoi(intB, 'left', 'mid', 'right')
