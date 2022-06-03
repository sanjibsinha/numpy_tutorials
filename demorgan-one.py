def notAandB(paramOne, paramTwo):
    additionOfTwoNumbers = paramOne + paramTwo
    if((paramOne <= 10 and paramTwo >= 15)):
        print(f'Addition of two numbers : {additionOfTwoNumbers}')
    else:
        print(f'The number is neither less than equal to 10 nor greater than equal to 15')
     

def notAORnotB(paramOne, paramTwo):
    additionOfTwoNumbers = paramOne + paramTwo
    if((paramOne <= 10 or paramTwo >= 15)):
        print(f'Addition of two numbers : {additionOfTwoNumbers}')
    else:
        print(f'The number is neither less than equal to 10 nor greater than equal to 15')
           
    
notAandB(1, 14)
notAandB(1, 140)
notAORnotB(1, 14)
notAORnotB(1, 140)

'''
The number is neither less than equal to 10 nor greater than equal to 15
Addition of two numbers : 141
Addition of two numbers : 15
Addition of two numbers : 141
'''


    

    
    
    
    
 

