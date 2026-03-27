"""
Python While Loop Exercise

Part 1 – Basic Level

1. Print numbers from 1 to 10 using a while loop.

i = 1
while i < 11:
    print(i)
    i+=1


2. Print even numbers from 1 to 20.

i = 1
while i < 21:
    if i%2==0:
        print(i)
    i+=1


3. Print odd numbers from 1 to 20.

i = 1
while i < 21:
    if i%2!=0:
        print(i)
    i+=1


4. Print numbers from 10 to 1 (reverse order).

i = 10
while i > 0:
    print(i)
    i-=1

5. Print multiplication table of 5 using while loop.

i = 1
while i < 11:
    print(i*5)
    i+=1



Part 2 – Intermediate Level

6. Find the sum of first 10 natural numbers using while loop.

i = 1
sum = 0
while i<11:
    sum+=i
    i+=1
print(sum)


7. Find factorial of a number entered by user.

num = int(input("Enter a number to find it Factorial: "))
factorial = 1
while num>0:
    factorial = factorial*num
    num-=1
print(factorial)
    

8. Count number of digits in a given number.

num = int(input("Enter a Number: "))
digits = 0
while num>0:
    num=num//10
    digits+=1
print(digits)
    


9. Reverse a number using while loop.

num = int(input("Enter a Number: "))
reverse  = 0
while num>0:
    digit = num%10
    reverse = reverse*10 + digit
    num = num//10
print(reverse)


10. Check whether a number is palindrome or not using while loop.

num = int(input("Enter a Number to Check: "))
original_num = num
reverse = 0
while num>0:
    a = num%10
    reverse = reverse*10+a
    num = num//10
if original_num == reverse:
    print("It is a Pelindrome.")
else:
    print("It is Not a Pelindrome")

Part 3 – Pattern Based

11. Print pattern: 
* 
** 
*** 
**** 
*****

i = 1
while i < 6:
    print(i*"*")
    i+=1


12. Print pattern: 
1 
12 
123 
1234 
12345

i = 1
while i < 6:
    j = 1
    while j<=i:
        print(j, end = "")
        j+=1
    print()
    i+=1


Part 4 – Logical / Real Scenario

13. Ask user to enter password until correct password is entered.

password = "abhii"
print("Login to Continue...")
i = 1
while password:
    user = input("Enter your Password: ")
    if password == user:
        print("Login Succesfull...!")
        break
    else:
        print("Wrong Password...! Please Re-Enter your Password...")
    i+=1

14. Create a number guessing game: 
• Generate a random number (1–10) 
• Keep asking user until they guess correctly

import random

random_num = random.randint(1,10)
i = 1
while random_num:
    user_num = int(input("Guess a Number between 1-10: "))
    if user_num == random_num:
        print("You Guessed it Right...!")
        break
    else:
        print("Wrong Guess...! Again Guess a Number: ")
    i+=1


15. Keep taking input numbers until user enters 0, then print total sum.

total_sum = 0
i = 1
while i==1:
    user_num = int(input("Enter a Number: "))
    total_sum = total_sum+user_num
    if user_num == 0:
        print("Total Sum: ",total_sum)
        break


Bonus Challenge (Interview Level)

16. Print Fibonacci series up to N terms using while loop.

a, b = 0, 1
n = int(input("Enter number of terms: "))
i = 0
while i<=n:
    c = a+b
    print(c)
    a = b
    b = c
    i+=1

17. Check whether a number is Armstrong number.



18. Print prime numbers between 1 to 50 using while loop.

num = 2

while num<=50:
    i = 2
    is_prime = True

    while i<num:
        if num%i==0:
            is_prime = False
            break
        i+=1
    if is_prime:
        print(num)

    num+=1
    
"""


    











    



