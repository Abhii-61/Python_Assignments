"""
Q1. Print Numbers 
Use a for loop to print numbers from 1 to 10.

for i in range(1,11):
    print(i)


Q2. Print Even Numbers 
Print all even numbers between 1 and 20.

for i in range(1,21):
    if i%2==0:
        print(i)


Q3. Find Sum 
Print the sum of numbers from 1 to 10 using a for loop.

sum = 0
for i in range(1,11):
    sum = sum+i
print(sum)



Q4. Multiplication Table 
Take a number from the user and print its multiplication table up to 10.

num = int(input("Enter the Number: "))
for i in range(1,11):
    print(num * i)



Q5. Count Characters 
Take a string and count the total number of characters using a for loop.

word = input("Enter a String: ")
count = 0

for i in word:
    count+=1
print(count)



PART 2 – Break Related Questions

Q6. Stop at 5 
Print numbers from 1 to 10. 
Stop the loop when the number becomes 5.

for i in range(1,11):
    print(i)
    if i == 5:
        break



Q7. Search in List 
Search for number 25 in a list. 
If found, print "Found" and stop the loop.

nums = [1,2,5,12,15,18,21,22,25,27,30]

for i in nums:
    print(i)
    if i == 25:
        print("Found", i)
        break



Q8. First Negative Number 
Given a list of numbers, print the first negative number and stop the loop.

nums = [1,2,3,-4,-5,6,-7,8]

for i in nums:
    print(i)
    if i<0:
        print("Found first Negative number:", i)
        break



PART 3 – Continue Related Questions

Q9. Skip 5 
Print numbers from 1 to 10.
Skip number 5.

for i in range(1,11):
    if i == 5:
        continue
    print(i)



Q10. Skip Even Numbers 
Print numbers from 1 to 20. 
Skip all even numbers.

for i in range(1,21):
    if i%2==0:
        continue
    print(i)
    



Q11. Skip Letter
Print each character of the string "PYTHON". 
Skip the letter "O".


word = "PYTHON"

for i in word:
    if i == "O":
        continue
    print(i)


 
PART 4 – Pass Related Questions 
 
Q12. Empty Loop 
Run a loop from 1 to 5 but do nothing inside the loop using pass.

for i in range(1,6):
    pass



 
Q13. Skip Using Pass 
Loop from 1 to 10. 
If number is 6, just use pass.

for i in range(1,11):
    if i == 6:
        pass


 
PART 5 – For-Else Questions 
(Remember: else runs only if the loop is not stopped by break.) 
 
Q14. Search Number Using for-else 
Search for number 100 in a list. 
If found, print "Found". 
If not found, print "Not Found".


nums = [10,20,50,80,100,120,200,400]

for i in nums:
    if i == 100:
        print("Found the Number 100")
        break
    else:
        print("Not Found the Numbar 100")


 
Q15. Prime Number Check 
Take a number from the user and check whether it is prime using for-else. 
 
num = int(input("Enter a Number to check: "))
factors = 0

for i in range(1, num+1):
    if num%i == 0:
        factors+=1
if factors == 2:
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")


 
 
PART 6 – Pattern Questions 
 
Q16. Star Pattern 
Print: 
* 
** 
*** 
**** 
*****

for i in range(1,6):
    for j in range(i):
        print("*", end = "")
    print()


 
Q17. Reverse Star Pattern 
Print: 
***** 
**** 
*** 
** 
*

for i in range(6,1,-1):
    for j in range(i):
        print("*", end = "")
    print()



 
Q18. Number Pattern 
Print: 
1 
12 
123 
1234 
12345 

for i in range(1,6):
    for j in range(i):
        print(j+1, end = "")
    print()


 
 
Q19. Same Number Pattern 
Print: 
1 
22 
333 
4444 
55555 

for i in range(1,6):
    for j in range(i):
        print(i, end = "")
    print()



 
Q20. Pyramid Pattern 
Print: 
        * 
      *** 
    ***** 
  ******* 
********* 





 
Q21. Inverted Pyramid 
Print: 
********* 
  ******* 
    ***** 
      *** 
        *




        
 
Bonus Question 
Q22. Break in Pattern 
Print a star pattern. 
Stop printing when the row number reaches 4.
"""

for i in range(9,0,-2):
    for j in range(i):
        print("*", end ="")
    print()






















