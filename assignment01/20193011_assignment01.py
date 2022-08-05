data = []

# 파일에서 불러 오는 부분
with open('./미로/maze2.txt') as f:
    size = f.readline()[:-1]
    while True:
        line = f.readline()
        if not line: break
        if '\n' in line:
            if '\n' != line:
                data.append(line[:-1])
        else:
            data.append(line)
# 불러온 파일의 내용을 우선 data 변수에 담는다. 

width=len(data[0])
height=len(data)

# 미로 저장하는 함수
def make_maze(maze, width, height):
    newmaze = []
    for row_idx in range(0, height-1, 2):
        row_data = []   
        for col_idx in range(0, width-1, 2):
            if maze[row_idx][col_idx+1] == '-' and maze[row_idx+1][col_idx] == '|' :
                row_data.append(3)
            elif maze[row_idx][col_idx+1] == '-' and maze[row_idx+1][col_idx] == ' ':
                row_data.append(1)
            elif maze[row_idx][col_idx+1] == ' ' and maze[row_idx+1][col_idx] == '|':
                row_data.append(2)
            elif maze[row_idx][col_idx+1] == ' ' and maze[row_idx+1][col_idx] == ' ':
                row_data.append(0)
        row_data.append(2)
        newmaze.append(row_data)
    newmaze.append([1]*int((len(data[0])-1)/2) +[0])
    return newmaze

# 미로 화면에 표시
def draw_maze(newmaze):
    character = [' ', '-', '|', '+']
    draw=[]
    for row_idx in range(len(newmaze)):
        up_data = []
        low_data = []
        for col_idx in range(len(newmaze[0])):

            if newmaze[row_idx][col_idx] == 0 :
                up_data.append(character[3] + character[0])
                low_data.append(character[0] + character[0])

            elif newmaze[row_idx][col_idx] == 1 :  #'+-'
                low_data.append(character[0] + character[0])

                if (col_idx > 0) and (row_idx > 0) and \
                ((newmaze[row_idx][col_idx-1] == 1) or (newmaze[row_idx][col_idx-1] == 3)) and \
                ((newmaze[row_idx-1][col_idx] == 0) or (newmaze[row_idx-1][col_idx] == 1)):
                    up_data.append(character[1] + character[1])
                elif row_idx == 0 :
                    up_data.append(character[1] + character[1])

                else:
                    up_data.append(character[3] + character[1])

            elif newmaze[row_idx][col_idx] == 2 :
                low_data.append(character[2] + character[0])

                if (col_idx > 0 ) and (row_idx > 0) and \
                ((newmaze[row_idx][col_idx-1] == 0 ) or (newmaze[row_idx][col_idx-1] == 2)) and \
                ((newmaze[row_idx-1][col_idx] == 2) or (newmaze[row_idx-1][col_idx] == 3)):
                    up_data.append(character[2] + character[0])
                elif col_idx == 0 :
                    up_data.append(character[2] + character[0])
                else:
                    up_data.append(character[3] + character[0])
            elif newmaze[row_idx][col_idx] == 3 :
                up_data.append(character[3] + character[1])
                low_data.append(character[2] + character[0])

            up = ''.join(up_data)
            low = ''.join(low_data)
        draw.append(up[:-1])
        draw.append(low[:-1])
    
    for i in range(len(draw)):
        print(draw[i])
        
newmaze = make_maze(data , width , height)
draw_maze(newmaze)