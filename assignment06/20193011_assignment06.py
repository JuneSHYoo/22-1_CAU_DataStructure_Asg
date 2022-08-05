import string

# 데이터 읽기
dictionary = []
with open('randdict.TXT', 'r') as file: 
    for text in file:
        dictionary.append(text.strip('\n').split(' : '))
        
# 연결리스트 클래스
class Node :
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def getNode(self, pos):
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None :
            node = node.next
            pos -= 1
        return node

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        self.len += 1
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node=Node(elem, before.next)
            before.next = node

    def delete(self, pos):
        before = self.getNode(pos-1)
        removed = before.next
        before.next = before.next.next
        self.len -=1 
        del removed

    def display(self):
        node = self.head.next
        while node is not None:
            print(node.data, end="->\n")
            node = node.next
        print()
        
# 데이터를 정렬하면서 연결리스트 구성하는 함수
def insert_sorted(linkedlist, text):
    node = linkedlist.head
    pos = 0
    while 1:
        data = node.data
        transform_data_key = data[0].lower()
        transform_text_key = text[0].lower()

        if transform_data_key > transform_text_key:
            linkedlist.insert(pos,text)
            break

        if node.next == None:
            linkedlist.insert(pos+1,text)
            break

        node = node.next
        pos += 1
        
    return linkedlist

## 사전 만들기 (개선 후 방법)
# 단어 시작하는 앞글자 별로 연결리스트 사전 생성
linkedlists = {}
for alphabet in string.ascii_lowercase:
    linkedlists[alphabet] = LinkedList()
    
for text in dictionary:
    linkedlist = linkedlists[text[0].lower()[0]]
    
    if linkedlist.head == None:
        linkedlist.insert(0, text)
        
    else:
        linkedlist = insert_sorted(linkedlist, text)
        
# 단어 검색 및 추가 기능
word = input('단어를 검색하세요. : ')

linkedlist = linkedlists[word.lower()[0]]
node = linkedlist.head
while 1:
    data = node.data
    
    if data[0] == word :
        print(data[1])
        break
    
    if node.next != None :
        node = node.next
    else:
        meaning = input("찾을 수 없는 단어입니다. 뜻을 추가하세요. (추가하지 않으려면 공백) : ")
        if meaning == '':
            break
        text = [word, meaning]
        linkedlist = insert_sorted(linkedlist, text)
        print(f'{word} {meaning} 가 추가되었습니다. (총 {linkedlist.len}개 단어)')
        break