import random
import string
import time

##  (1) 데이터 생성하기
def student_data():
    data = [] 
    
    st_id = [] #학번 8자리 저장할 데이터
    st_yr = [2019,2020, 2021, 2022]  #입학년도
    for i in st_yr:
        id_b = random.sample(range(10000), 5000)
        for j in range(5000):
            id_b[j]= str(i) +'%04d'%id_b[j]
        st_id += id_b
    random.shuffle(st_id)

    for i in range(20000):
        student = []
        student.append(st_id[i])

        st_name = ''
        for j in range(10):
            st_name += str(random.choice(string.ascii_uppercase))
        student.append(st_name)

        st_phone = '010'+'%08d'%random.randint(0,99999999)
        student.append(st_phone)

        data.append(student) 
        
    return data 



# 중복 발견하는 함수
def id_rep_check(st_data):
    rep = False
    for i in range(len(st_data)-1):
        for j in range(i+1, len(st_data)):
            if (st_data[i][0][0:4] == '2019') and (st_data[j][0][0:4] == '2019') :
                if st_data[i][0][4:10] == st_data[j][0][4:10]:
                    rep = True
                    break

            elif (st_data[i][0][0:4] == '2020') and (st_data[j][0][0:4] == '2020') :
                if st_data[i][0][4:10] == st_data[j][0][4:10]:
                    rep = True
                    break
            elif (st_data[i][0][0:4] == '2021') and (st_data[j][0][0:4] == '2021') :
                if st_data[i][0][4:10] == st_data[j][0][4:10]:
                    rep = True
                    break
            elif (st_data[i][0][0:4] == '2022') and (st_data[j][0][0:4] == '2022') :
                if st_data[i][0][4:10] == st_data[j][0][4:10]:
                    rep = True
                    break
        if rep == True:
            print("중복 발견")
            break
        else:
            print("중복 없음")
            break
        
# 함수가 잘 작동하는지 확인

rep_test = [['20200249', 'EFQWURSRWA', '01000781634'],
 ['20200249', 'CXRXUOQIWS', '01093779800'],
 ['20216397', 'TIFBRUJTAX', '01099541227'],
 ['20221295', 'YVZQNWACAZ', '01005467894'],
 ['20193110', 'XGMROJSHHC', '01056575793']]   #첫번째와 두번째 학생의 학번이 동일하게 설정

print(">> rep_test 데이터 :")
for i in range(len(rep_test)):
    print(rep_test[i])
print(">> 'rep_test 데이터' 중복 확인 결과 => " , end= '')
id_rep_check(rep_test)

# 학생 데이터 생성하고 중복 확인하기
st_data = student_data()
data = st_data

print(">> 학생 데이터 (2000명당 1개 출력) :")
for i in range(len(data)):
    if i % 2000 == 0:
        print(data[i])
    else:
        continue
print(">> '학생 데이터' 중복 확인 결과 => " , end= '')
id_rep_check(data)

## (2) 내장된 정렬 함수로 정렬하기 
data = st_data
print("<Python 내장 함수로 정렬하기>")

#학번 기준으로 정렬
print("> 학번 기준 정렬")
start = time.time()
data.sort(key = lambda x: x[0])
finish = time.time()

pyth_sort_id_time = finish-start

# 정렬이 잘 되어있는지 확인
print(">> 정렬 결과 (2000명당 1개 출력)")
for i in range(len(data)):
    if i % 2000 == 0 :
        print(data[i])
    else:
        continue
print(">> 내장된 함수로 정렬하는데 소요된 시간은 {}초 입니다." .format(pyth_sort_id_time))

#이름 기준으로 정렬
data = st_data
print("> 이름 기준 정렬")
start = time.time()
data.sort(key = lambda x: x[1])
finish = time.time()

pyth_sort_name_time = finish-start

# 정렬이 잘 되어있는지 확인
print(">> 정렬 결과 (2000명당 1개 출력)")
for i in range(len(data)):
    if i % 2000 == 0 :
        print(data[i])
    else:
        continue
print(">> 내장된 함수로 정렬하는데 소요된 시간은 {}초 입니다." .format(pyth_sort_name_time))


## (3) 선택정렬, 퀵정렬, 힙정렬
# 선택 정렬 함수
def selection_sort(data, criterion):
    n = len(data)
    for i in range(n-1):
        least = i 
        for j in range(i+1, n):
            if data[j][criterion] < data[least][criterion]:
                least = j
        data[i], data[least] = data[least] , data[i]
    return data

# 선택 정렬 결과
data = st_data
print("<선택 정렬로 정렬하기>")

#학번 기준으로 정렬
print("> 학번 기준 정렬")
start = time.time()
selection_sort(data, 0)
finish = time.time()

selection_sort_id_time = finish-start

# 정렬이 잘 되어있는지 확인
print(">> 정렬 결과 (2000명당 1개 출력)")
for i in range(len(data)):
    if i % 2000 == 0 :
        print(data[i])
    else:
        continue
print(">> 선택 정렬하는데 소요된 시간은 {}초 입니다." .format(selection_sort_id_time))

#이름 기준으로 정렬
data = st_data
print("> 이름 기준 정렬")
start = time.time()
selection_sort(data, 1)
finish = time.time()

selection_sort_name_time = finish-start

# 정렬이 잘 되어있는지 확인
print(">> 정렬 결과 (2000명당 1개 출력)")
for i in range(len(data)):
    if i % 2000 == 0 :
        print(data[i])
    else:
        continue
print(">> 선택 정렬하는데 소요된 시간은 {}초 입니다." .format(selection_sort_name_time))

# 퀵 정렬 함수
def quick_sort(data, low, high, criterion):
    if low < high:
        pivot = partition(data, low, high , criterion)
        quick_sort(data, low, pivot-1, criterion)
        quick_sort(data, pivot+1, high, criterion)
    
    return data

def partition(data, pivot, high, criterion):
    i = pivot+1
    j = high
    
    while True:
        while i < high and data[i][criterion] < data[pivot][criterion]:
            i+=1
        while j > pivot and data[j][criterion] > data[pivot][criterion]:
            j-=1
        if j <= i :
            break
        
        data[i] , data[j] = data[j], data[i] 
        i+=1
        j-=1
    data[pivot] , data[j] = data[j] , data[pivot]
    
    return j

# 퀵 정렬 결과
data = st_data
print("<퀵 정렬로 정렬하기>")

#학번 기준으로 정렬
print("> 학번 기준 정렬")
start = time.time()
quick_sort(data, 0 , len(data)-1, 0) 
finish = time.time()

quick_sort_id_time = finish-start

# 정렬이 잘 되어있는지 확인
print(">> 정렬 결과 (2000명당 1개 출력)")
for i in range(len(data)):
    if i % 2000 == 0 :
        print(data[i])
    else:
        continue
print(">> 퀵 정렬하는데 소요된 시간은 {}초 입니다." .format(quick_sort_id_time))

#이름 기준으로 정렬
data = st_data
print("> 이름 기준 정렬")
start = time.time()
quick_sort(data, 0 , len(data)-1, 1) 
finish = time.time()

quick_sort_name_time = finish-start

# 정렬이 잘 되어있는지 확인
print(">> 정렬 결과 (2000명당 1개 출력)")
for i in range(len(data)):
    if i % 2000 == 0 :
        print(data[i])
    else:
        continue
print(">> 퀵 정렬하는데 소요된 시간은 {}초 입니다." .format(quick_sort_name_time))

# 힙 정렬 함수
def adjust(data, root, size, criterion):     #힙 정렬의 한단계 실행
    while 2*root+1 <= size :    #한 root의 child가 없을 때까지 반복
        child = 2*root+1
        if (child < size) and data[child][criterion] < data[child+1][criterion]:  # child에서 큰쪽을 찾아서 힙 정렬 실행
            child+=1
        if data[root][criterion] >= data[child][criterion]:  #child의 수보다 root의 수가 크면 swap 하지 않고 break
            break 
        
        data[root] , data[child] = data[child] , data[root]  # child의 값이 더 크면 root에 큰 값이 오도록 바꿔준다. 
        root = child

def heap_sort(data, criterion):      #힙 정렬을 하는 함수
    size = len(data)-1               #힙의 총 사이즈 
    for i in reversed(range(0, (size+1)//2-1)): # 트리의 아래부터 adjust 함수를 통해 root에 가장 큰 값잉 나오도록 정렬
        adjust(data, i , size, criterion) 
    
    for j in range(size):
        data[0] , data[size] = data[size] , data[0]   #루트의 값(가장 큰 값)을 트리의 끝으로 보낸다.
        size -= 1                                     #트리의 사이즈를 1 줄여 가장 마지막 값(큰 값)을 제외하고 힙 정렬
        adjust(data, 0, size, criterion) 
        
        
# 힙 정렬 결과
data = st_data
print("<힙 정렬로 정렬하기>")

#학번 기준으로 정렬
print("> 학번 기준 정렬")
start = time.time()
heap_sort(data, 0)
finish = time.time()

heap_sort_id_time = finish-start

# 정렬이 잘 되어있는지 확인
print(">> 정렬 결과 (2000명당 1개 출력)")
for i in range(len(data)):
    if i % 2000 == 0 :
        print(data[i])
    else:
        continue
print(">> 힙 정렬하는데 소요된 시간은 {}초 입니다." .format(heap_sort_id_time))

#이름 기준으로 정렬
data = st_data
print("> 이름 기준 정렬")
start = time.time()
heap_sort(data, 1)
finish = time.time()

heap_sort_name_time = finish-start

# 정렬이 잘 되어있는지 확인
print(">> 정렬 결과 (2000명당 1개 출력)")
for i in range(len(data)):
    if i % 2000 == 0 :
        print(data[i])
    else:
        continue
print(">> 힙 정렬하는데 소요된 시간은 {}초 입니다." .format(heap_sort_name_time))
