import copy
import pandas as pd

# stack 정의
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
            
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    
    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0 
    
    def __str__(self):
        return str(self.items[::-1])
    
# 미로 파일 불러오기
data = []
with open('./미로/maze1.txt') as f:
    size = f.readline()[:-1]
    while True:
        line = f.readline()
        if not line: break
        if '\n' in line:
            if '\n' != line:
                data.append(line[:-1])
        else:
            data.append(line)

for i in range(len(data)):
    print(data[i])
            
# maze 방향에 따라 표시
def newmaze(data):
    new_maze = []
    for row_idx in range(1, len(data), 2 ):
        row = []
        for col_idx in range(1, len(data[0]), 2):
            move = [0,0,0,0]
            if data[row_idx][col_idx+1] == ' ' : #동
                move[0] = 1
            if data[row_idx][col_idx-1] == ' ' : #서
                move[1] = 1
            if data[row_idx+1][col_idx] == ' ' : #남
                move[2] = 1
            if data[row_idx-1][col_idx] == ' ' : #북
                move[3] = 1
            row.append(move)
        new_maze.append(row)
    return new_maze

new_maze = newmaze(data)

# 경로를 미로에 그리는 함수
def print_maze(data, path):
    copy_data = data.copy()
    for p in path:
        row = list(copy_data[p[0]*2+1])
        row[p[1]*2+1] = "O"
        copy_data[p[0]*2+1]= ''.join(row)
        
    for i in range(len(copy_data)):
        print(copy_data[i])
        
## 미로 길찾기 알고리즘
path = Stack() # 지나온 경로
stack = Stack() # 갈림길에서 좌표랑 방향
save_path = [] # 출구까지 도달했을때의 path 저장하는 리스트

#시작 좌표는 0,0이다.
row_idx = 0 
col_idx = 0 

# 출구 좌표 설정하기
end_row_idx = len(new_maze)-1
end_col_idx = len(new_maze[0])-1

poped = False
while 1: 
    
    if poped == False:
        move = new_maze[row_idx][col_idx].copy()
    poped = False
    
    # 어디서 왔는지 확인하고 지나온 길은 못가게 막는다.
    if path.isEmpty() == False:
        if path.top()[1] > col_idx : move[0] = 0
        if path.top()[1] < col_idx : move[1] = 0
        if path.top()[0] > row_idx : move[2] = 0
        if path.top()[0] < row_idx : move[3] = 0
    
    # 다시 시작점(0,0)으로 돌아가 무한반복 막는다.
    if row_idx == 0 and col_idx == 1 :
        move[1] = 0
    if row_idx == 1 and col_idx == 0 :
        move[3] = 0
    
    # 현재 위치를 경로 스택에 넣기
    path.push([row_idx, col_idx])
    
    # 현재 위치가 출구 좌표라면 현재 현재 까지의 경로 하나를 save_path 리스트에 넣어준다.
    if row_idx == end_row_idx and col_idx == end_col_idx:
        save_path.append(path.items.copy())
    
    # 가는거
    if sum(move) == 1: # 가는 길이 하나일 때
        if move[0] == 1 : col_idx += 1
        if move[1] == 1 : col_idx -= 1
        if move[2] == 1 : row_idx += 1
        if move[3] == 1 : row_idx -= 1

    elif sum(move) > 1 : # 가는 길이 여러개 일때 동,서,남,북 순으로 이동 한후 지나왔던 방향은 막기
        print(f"PUSH({row_idx},{col_idx})")
        if move[0] == 1 :
            move[0] = 0
            stack.push([row_idx, col_idx, move])
            col_idx += 1
        elif move[1] == 1:
            move[1] = 0
            stack.push([row_idx, col_idx, move])
            col_idx -= 1
        elif move[2] == 1:
            move[2] = 0
            stack.push([row_idx, col_idx, move])
            row_idx += 1
        elif move[3] == 1:
            move[3] = 0
            stack.push([row_idx, col_idx, move])
            row_idx -= 1
            
    elif sum(move) == 0 : # 모든 방향이 막혔을때 
        
        if stack.isEmpty(): # 돌아갈 갈림길이 없으면 반복문 중단 및 현재까지 찾은 경로개수 출력
            print(f"모두 {len(save_path)}개의 길을 찾았습니다.")
            break
        
        poped = True  # 갈림길로 돌아갔기 때문에 pop변수 true로 변환
        row_idx, col_idx, move = stack.pop() 
        print(f"POP({row_idx},{col_idx})")
        while 1: # 갈림길로 부터 막다른 길까지의 경로 다 지우기 
            if path.top()[0] == row_idx and path.top()[1] == col_idx: # 갈림길 위치까지 반복문을 통해 좌표 지우기
                break
            path.pop()

# 경로 표시하기
for path in save_path:
    print(f"경로 {save_path.index(path)+1}/{len(save_path)}")
    print_maze(data, path)
    print("=====================")