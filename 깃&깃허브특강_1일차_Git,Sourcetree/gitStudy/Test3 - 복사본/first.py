## 메서드 선언부
def add_func(n1, n2) :
    res = n1 + n2
    return res
def subt(n1, n2) :
    res = n1 - n2
    return res
def mul_func(n1, n2) :
    res = n1 * n2
    return res
#def div_func(n1, n2) :
#   res = n1 / n2
#    return res
def double_func(n1, n2) :
    res = n1 ** n2
    return res
## 전역 변수(인스턴스변수, 클래스변수)
num1, num2, result = 100, 200, 0

## 메인 코드부( main() 메서드 )
# result = num1+num2
result = add_func(num1, num2)
result2 = subt(num1, num2)
result3 = mul_func(num1, num2)
#result4 = div_func(num1, num2)
result5 = double_func(num1, num2)
print(num1, '+', num2, '=', result)
print(num1, '-', num2, '=', result2)
print(num1, '*', num2, '=', result3)
#print(num1, '/', num2, '=', result4)
print(num1, '**', num2, '=', result5)

