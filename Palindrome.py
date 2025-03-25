#Palindrome

def checkPalindrome(number):
    temp = number
    output = 0
    while number != 0:
        #to get last digit
        lastdigit = number % 10
        output= (output*10) + lastdigit
        #to remove the last digit
        number = number // 10
        if output == temp:
            return f'{temp} is palindrome'
        else:
            return f'{temp} is not a palindrome'
        
number = int(input("Enter a number to check its palindrome or not...\n"))
print(checkPalindrome(number))