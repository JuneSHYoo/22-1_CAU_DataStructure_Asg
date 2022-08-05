dictionary = []
with open('randdict.TXT', 'r') as file: 
    for text in file:
        dictionary.append(text.strip('\n').split(' : '))
    
class Node :
    def __init__(self, data, left=None, right = None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None 
    
    ## 이진 탐색 트리의 탐색
    
    def search(self, item):
        if self.root.data is None:
            return None
        else:
            level = 1
            return self.__search_node(self.root, item , level) 
        
    def __search_node(self, cur, item, level):
        if cur is None:
            return None
        
        data = cur.data
        data_key = data[0]
        
        if data_key == item:
            return cur, level
        else:
            if data_key >= item:
                level += 1
                return self.__search_node(cur.left , item, level)
            else:
                level += 1
                return self.__search_node(cur.right, item, level)
        return None
    
    ## 이진 탐색 트리의 삽입
    
    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self.__insert_node(self.root , item)
    
    def __insert_node(self, cur, item):
        data = cur.data
        transform_data_key = data[0].lower()
        transform_item_key = item[0].lower()
        
        if transform_data_key >= transform_item_key :
            if cur.left is not None:
                self.__insert_node(cur.left, item)
            else:
                cur.left = Node(item)
        else:
            if cur.right is not None:
                self.__insert_node(cur.right, item) 
            else:
                cur.right = Node(item)

# 오름차순 출력
def inorder(n):
    if n!= None:
        inorder(n.left)
        print(n.data)
        inorder(n.right)
        
#트리 높이 세기
def calc_height(n):
    if n is None: return 0
    return 1+max(calc_height(n.left),calc_height(n.right))

#트리 노드 개수 세기
def count_node(n):
    if n is None: return 0
    return 1+count_node(n.left) + count_node(n.right)
        
        
# 최소 높이 사전 탐색 트리 만들기

dict_tree = BinaryTree()

for word in dictionary:
    dict_tree.insert(word)

## A 트리를 이용해 사전 정렬하기
sorted_dictionary = []
def sort_inorder(n):
    if n!= None:
        sort_inorder(n.left)
        sorted_dictionary.append(n.data)
        sort_inorder(n.right)
        
sort_inorder(dict_tree.root)
        
## 정렬된 사전으로 최소 높이 트리 만드는 함수
def insert_comptree(dict_sample):
    if len(dict_sample) == 1:
        dict_comp_tree.insert(dict_sample[0])
    
    elif len(dict_sample) > 1: 
        idx = len(dict_sample)//2
        dict_comp_tree.insert(dict_sample[idx])

        insert_comptree(dict_sample[:idx])
        insert_comptree(dict_sample[idx+1:])

dict_comp_tree = BinaryTree()

insert_comptree(sorted_dictionary)

print(f"사전 파일을 모두 읽었습니다. {len(dictionary)} 개의 단어가 있습니다. \nB 트리의 전체 높이는 {calc_height(dict_comp_tree.root)}입니다. B 트리의 노드 수는 {count_node(dict_comp_tree.root)}개 입니다. ")


while 1:
    word = input('단어를 입력하세요.: ')
    if dict_comp_tree.search(word) is not None:
        node, level = dict_comp_tree.search(word)
        print(f"{node.data[1]} (레벨 {level})")
    else:
        print("사전에 단어가 없습니다.")