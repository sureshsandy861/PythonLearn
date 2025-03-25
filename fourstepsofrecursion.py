#Palindrome
"""
number = int(input("Enter a number to check its palindrome or not...\n"))
temp = number
output = 0
while number != 0:
    #to get last digit
    lastdigit = number % 10
    output= (output*10) + lastdigit
    #to remove the last digit
    number = number // 10
    if output == temp:
        print(f'{temp} is palindrome')
    else:
        print(f'{temp} is not a palindrome')
        
"""

#First you need know to write the code in while loop
"""
Step 1 : Initialization of looping variables should be done when creating the formal agrument in function
step 2 : The terminate condition exactly oppsite to the loop (while) condition
step 3 : Write out the logic of the program
step 4 : The Updation and send the value for the next iteration in recursive call itself

"""


        

def checkPalindrome(number , temp, output):
    if number == 0:
        if output == temp:
            return f'{temp} is palindrome'
        else:
            return f'{temp} is not a palindrome'
    lastdigit = number % 10
    output= (output*10) + lastdigit
    number = number // 10
    return checkPalindrome(number, temp , output)

number = int(input("Enter a number to check its palindrome or not...\n"))
temp =number
print(checkPalindrome(number, temp , 0))
