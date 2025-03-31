#RangeOfPalindrome

def checkPalindrome(starNumber,endNumber):
    result = []
    while starNumber <= endNumber:
        temp = starNumber
        output = 0
        number = temp
        while number != 0:
            #to get last digit
            lastdigit = number % 10
            output= (output*10) + lastdigit
            #to remove the last digit
            number = number // 10
            if output == temp:
                result = result +[output]
        starNumber+= 1
    return f'{result} this list of number is palindrome in the given range'
        
starNumber = int(input("Enter a starting number...\n"))
endNumber = int(input("Enter a ending number...\n"))
print(checkPalindrome(starNumber,endNumber))
