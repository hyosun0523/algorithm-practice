def arrinput():#함수 입력
    arr = list(map(int,input('값 입력:').split()))
    return arr

def ssort(arr):#선택정렬
    for i in range(0, len(arr)-1):
        key = i #정렬할 자리(기준 설정)
        for j in range(i+1, len(arr)):#최솟값 탐색
            if(arr[key]>arr[j]):#최솟값 인덱스 결정
                key = j
        arr[i], arr[key] = arr[key], arr[i]#값 교환
    return arr#정렬된 배열 반환
        
def isort(arr):#삽입정렬
    for i in range(1, len(arr)):
        key = arr[i] #자리 바꿀 값 선택
        j = i-1 #비교할 인덱스 번호(바꿀 값 앞자리 번호)
        while(j >= 0 and key<arr[j]):#j<0이면 위험, key 들어갈 자리 확보
            arr[j+1] = arr[j] #값 밀기
            j -= 1 #비교할 자리 변경
        arr[j+1] = key #인덱스 번호 하나 줄이는 걸로 마무리해서 j+1로 삽입할 자리 확정
    return arr#정렬된 배열 반환

def bsort(arr):#버블 정렬
    for i in range(0, len(arr)-1): #모든 자리 반복
        for j in range(0, len(arr) - i - 1): #마지막 값은 제자리를 찾음
            if(arr[j]>arr[j+1]): #인접 값 비교
                arr[j], arr[j+1] = arr[j+1], arr[j] #큰 값이 오른쪽으로
    return arr#정렬된 배열 반환

arrA = arrinput()
ssort(arrA)
print(arrA)

arrB = arrinput()
isort(arrB)
print(arrB)

arrC = arrinput()
bsort(arrC)
print(arrC)
