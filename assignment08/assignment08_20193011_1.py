## 사전 해싱하기

# 사전 파일 불러오기
dictionary = []
with open('randdict.TXT', 'r') as file: 
    for text in file:
        dictionary.append(text.strip('\n').split(' : '))
        
# 해시 함수 설정
def hash_function(word):
    sum = 0 
    for i in word:
        sum+=ord(i)**2
    sum = str(sum)[1:5]
    
    return int(sum)

# 해시 함수 테스트
'''
hash = []

for i in dictionary:
    ind = hash_function(i[0])
    hash.append(ind)
    
print('index 시작 : ', min(hash))
print('index 끝 : ', max(hash))
print('해시 테이블 버킷 수 : ', max(hash) - min(hash)+1)

cnt = [] 
for i in range(min(hash), max(hash)+1):
    cnt.append(hash.count(i))
    
print('해시 테이블 슬롯 수 : ', max(cnt))
'''

## 단어 검색하기 
# 해시 테이블 초기화
hash_table = [[] for i in range(10000)]

# 사전의 단어와 뜻을 해시 테이블에 넣기
for i in dictionary:
    ind = hash_function(i[0])
    hash_table[ind].append(i)



while 1:
    count = 0
    word = input('단어를 입력하세요 : ')
    ind = hash_function(word) 
    for i in range(len(hash_table[ind])):
        count += 1
        if hash_table[ind][i][0] == word :
            print(f"{hash_table[ind][i][1]} ({count}회 검색)")
            print()
            break