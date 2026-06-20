arr = list(map(int,input('저장할 값 입력:').split()))
n = int


def sel():
    for i in range (0,len(arr)-1):
        a = i
        for j in range(i+1,len(arr)):
            if (arr[j]<arr[a]):
                a = j
        arr[i], arr[a] = arr[a], arr[i]
               
sel()
print(arr)
            
           
            
