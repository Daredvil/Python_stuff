# Calculations to be faulted:
#                            45*8,33+34,90-23,89/41

n1=int(input('First number, sir:'))
n2=int(input('Second number, sir:'))
Operator=input("Choose operation:")
Product='*'
Sum='+'
Difference='-'
Division='/'

if n1==45:
    print("Here is your answer sir,",n1-n2)
elif n1 ==33:
    print("Here is your answer sir,",n1-n2)
elif n1 ==90:
    print("Here is your answer sir,",n1+n2)
elif n1 ==89:
    print("Here is your answer sir,",n1-n2)
elif Operator==Product:
    print("Here is your answer sir,",n1*n2)
elif Operator==Sum:
    print("Here is your answer sir,",n1+n2)
elif Operator==Difference:
    print("Here is your answer sir,",n1-n2)
elif Operator==Division:
    print("Here is your answer sir,",n1/n2)

else:
    print('Wrong operator')

print('Do your best sir.')


