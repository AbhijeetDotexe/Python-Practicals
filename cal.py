# write a python program which will keep adding a stream of numbers inputted by the user till
# the user press q to quit the calculator

sum=0
while(True):
    user_input= input('Enter the price or press q to quit : \n')
    if (user_input !='q'):
        sum=sum+int(user_input)
        print(f"Current Bill is {sum}")
    else:
        print("Thanks for using our Calculator")
        print(f"Your Bill Total is {sum} \n Thank You for Visiting our Store")
        break
