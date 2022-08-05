# 덧셈
def sum_poly_2(len_poly1, len_poly2,poly1, poly2):
    sum_coef = []
    sum_expo = []
    sum_list = []
    i = 0 
    j = 0
    while 1:
        if poly1[1::2][i] == poly2[1::2][j]:
            sum_coef.append(poly1[0::2][i]+poly2[0::2][j])
            sum_expo.append(poly1[1::2][i])
            i+=1
            j+=1
        elif poly1[1::2][i] < poly2[1::2][j]:
            sum_coef.append(poly2[0::2][j])
            sum_expo.append(poly2[1::2][j])
            j+=1
        else:
            sum_coef.append(poly1[0::2][i])
            sum_expo.append(poly1[1::2][i])
            i+=1
        if (i == len_poly1/2) and (j == len_poly2/2):
            break

    for i in range(len(sum_coef)):
        sum_list.append(sum_coef[i])
        sum_list.append(sum_expo[i])
    return sum_list

#곱셈
def mul_poly_2(len_poly1, len_poly2, poly1, poly2):
    mul_coef = []
    mul_expo = []

    for j in range(0, len_poly2 , 2):
        for i in range(0 , len_poly1 , 2):
            mul_coef.append(poly1[i]*poly2[j])
            mul_expo.append(poly1[i+1]+poly2[j+1])

    mul_list = []
    for expo in range(max(mul_expo), -1, -1):
        coef_sum = 0
        for i in range(len(mul_expo)):
            if expo == mul_expo[i]:
                coef_sum += mul_coef[i]

        if coef_sum != 0:
            mul_list.append(coef_sum)
            mul_list.append(expo) 
    return(mul_list)

# y값
def result_val(x_val): 
    poly3 = sum_poly_2(len(poly1), len(poly2), poly1, poly2)
    poly4 = mul_poly_2(len(poly1), len(poly2), poly1, poly2)
    polys = [poly1, poly2, poly3, poly4]
    poly = polys[x_val[0]-1]
    x = x_val[1]
    result = []
    for i in range(0, len(poly), 2):
        b = poly[i]*x**poly[i+1]
        result.append(b)
        result_val = sum(result) 
    return result_val   

# 실행

print("수식 1을 입력하세요.", end = " ")
poly1 = list(map(int, input().split()))

print("수식 2를 입력하세요" , end = " ")
poly2 = list(map(int, input().split()))

print("수식 1 + 2 는" , sum_poly_2(len(poly1), len(poly2), poly1, poly2))
print("수식 1*2 는", mul_poly_2(len(poly1), len(poly2), poly1, poly2))

print("수식에 값을 넣으세요. ")
x_val = list(map(int, input().split()))

print("결과값은", result_val(x_val))