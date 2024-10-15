from random import randint

print("------------- Welcome to the number guessing game -------------")

# Asking number from the user
number = int(input("Enter the number between 1 to 100: "))
# Storing a random integer from a given range
guess = randint(1,101)

count = 1

while True:

 if number == guess:
     print("Congratulation!! you guessed it in ",count," times")
     break
 elif number > guess:
     print("Number is big try with smaller number.....")
     number = int(input("Enter number: "))
     count+=1
 else:
     print("Number is small try with bigger number.....")
     number = int(input("Enter number: "))
     count+=1