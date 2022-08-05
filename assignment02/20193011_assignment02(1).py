# 덧셈
def sum_poly(len_poly1, len_poly2, poly1, poly2):
    poly_sum = []
    if len_poly1>len_poly2:
        for i in range(len_poly1 - len_poly2):
            poly_sum.append(poly1[i])
        for i in range(len_poly2):
            poly_sum.append(poly1[i+(len_poly1 - len_poly2)] + poly2[i])
        return poly_sum
    else:
        for i in range(len_poly2 - len_poly1):
            poly_sum.append(poly2[i])
        for i in range(len_poly1):
            poly_sum.append(poly2[i+(len_poly2 - len_poly1)] + poly1[i])
        return poly_sum
    
# 곱셈
def mul_poly(len_poly1, len_poly2, poly1, poly2):
    poly_mul = [0 for i in range(len_poly1+len_poly2-1)]
    for i in range(len_poly2):
        for j in range(len_poly1):
            poly_mul[i+j]+=poly2[i]*poly1[j]
    return poly_mul

# y값 계산
def result_val(x_val): 
    poly3 = sum_poly(len(poly1), len(poly2), poly1, poly2)
    poly4 = mul_poly(len(poly1), len(poly2), poly1, poly2)
    polys = [poly1, poly2, poly3, poly4]
    poly = polys[x_val[0]-1]
    x = x_val[1]
    result = []
    for i in range(len(poly)):
        b = poly[len(poly)-(i+1)]*x**i
        result.append(b)
        result_val = sum(result) 
    return result_val    

# 실행
print("수식 1을 입력하세요.", end = " ")
poly1 = list(map(int, input().split()))

print("수식 2를 입력하세요" , end = " ")
poly2 = list(map(int, input().split()))

print("수식 1 + 2 는" , sum_poly(len(poly1), len(poly2), poly1, poly2))
print("수식 1*2 는", mul_poly(len(poly1), len(poly2), poly1, poly2))

print("수식에 값을 넣으세요. ")
x_val = list(map(int, input().split()))

print("결과값은", result_val(x_val))