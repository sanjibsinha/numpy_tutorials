# (a is true and b is true) is not true = false
## true and true is true 

# (a is not true or b is not true) = false
## false or false is false

def notAandB(paramOne, paramTwo):
    additionOfTwoNumbers = paramOne + paramTwo
    if((paramOne <= 10 and paramTwo >= 15) != True):
        print(f'Addition of two numbers : {additionOfTwoNumbers}')
    else:
        print(f'The number is neither less than equal to 10 nor greater than equal to 15')
     

def notAORnotB(paramOne, paramTwo):
    additionOfTwoNumbers = paramOne + paramTwo
    if((paramOne <= 10 or paramTwo >= 15)):
        print(f'Addition of two numbers : {additionOfTwoNumbers}')
    else:
        print(f'The number is neither less than equal to 10 nor greater than equal to 15')
           
    
notAandB(1, 140)
notAORnotB(11, 14)

'''
The number is neither less than equal to 10 nor greater than equal to 15
The number is neither less than equal to 10 nor greater than equal to 15
'''


    

    
    
    
    
 

