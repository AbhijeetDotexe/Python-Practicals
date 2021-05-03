# calculate the factorial of a given number and count the number of trailing zero's in that factorial
def factorial(number):
    if number == 0 or number ==1:
        return 1
    else:
        return number* factorial(number-1)

def counting_zero(number):
   count = 0
   i=5
   while(number//i!=0):
        count +=(number//i)
        i*=5
   return count
if __name__ == '__main__':

     number =int(input('Enter a number : '))
     print(counting_zero(number))
