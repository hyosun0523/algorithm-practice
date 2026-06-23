def arrinput():
    arr = list(map(int,input('값 입력:').split()))
    return arr

def lsearch(arr, key):#선형탐색
    for i in range(0, len(arr)):
        if(key == arr[i]):
            return i #찾은 값 자리
    return None#찾은 값 자리
  
arrA = arrinput()
a = int(input('찾는 수 입력:'))
indexA = lsearch(arrA, a)
if(a == None):
    print('찾는 값이 없습니다!')
else:
    print(indexA)
