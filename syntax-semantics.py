# base of calculation with the help of if-else logic

print("Enter a number: ")
left = int(input())
print("Enter another number: ")
right = int(input())
result = 0
print("Enter any arithmetic operator like +, -, * and / for "
"addition, subtraction, multiplication and division respectively: ")
arithmeticOperator = str(input())

if(arithmeticOperator == '+'):
    result = left + right
elif(arithmeticOperator == '-'):
    result = left - right
elif(arithmeticOperator == '*'):
    result = left * right
elif(arithmeticOperator == '/'):
    if(right != 0):
        result = left / right
    else:
        print("Denominator is zero.")
else:
    print(arithmeticOperator + " is not recognized!")

if(arithmeticOperator == '/' and right == 0):
    print("The result is undefined.")
else:
    print(str(left) + " " + str(arithmeticOperator) + " " + str(right) + " = " + str(result))
    
'''
Enter a number: 
23
Enter another number: 
3
Enter any arithmetic operator like +, -, * and / for addition, subtraction, multiplication and division respectively: 
/
23 / 3 = 7.666666666666667
'''