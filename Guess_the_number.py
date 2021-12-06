# Just copy this program and run it

my_number=68
# (yeah,I know it hurts)

print("Total number of guesses you will get-\n5\n")
guesses=5
print("So,lets start\n")
while(1):
    guesses=guesses-1
    your_number=int(input('Enter your number-\n'))
    if your_number==my_number:
        print("Yooo-Hoooo you win")
        print('It took you',5-guesses,'guesses')
        break
    elif guesses==0:
        print("Sorry you ran out of guesses :(")
        break
    elif your_number==69:
        print('(NICE! but no)')
    elif 66<your_number<70:
        print('(You are super close ngl)')
    elif 63<your_number<71:
        print('(You are close)')
    elif guesses==4:
        print("(HINT:its less than 75 and greater than 21)")
    elif guesses==3:
        print("(HINT:the number is between 61 and 71)")
    elif guesses==1:
        print(guesses, "guess left\n")
        print('(HINT:the number to be guessed is just one step away from being nice)')
        continue
    print(guesses,"guesses left\n")


