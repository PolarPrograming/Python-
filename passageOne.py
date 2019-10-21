#Passage one
#Calculator

var1 = int(input("请输入第一个数字："))
var2 = int(input("请输入第二个数字："))
operator = input("请输入运算符（仅支持加减乘除运算）：")

if operator == "+":
    result = var1 + var2
elif operator == "-":
    result = var1 - var2
elif operator == "*":
    result = var1 * var2
elif operator == "/":
    result = var1 / var2

print("{}和{}做'{}'运算时，结果为{}".format(var1,var2,operator,result))
print("%d和%d做'%s'运算时，结果为%f" % (var1, var2, operator, result))
print("%d和%d做'%s'运算时，结果为%.2f" % (var1, var2, operator, result))
