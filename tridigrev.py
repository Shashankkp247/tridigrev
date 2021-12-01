#intro
print('"PROJECT DETAILS"\n~ Project name: 3_digit_number_reverser\n~ Creator name: Shashank.k.puttappanavar\n~ GitHub ID: Shashankkp247\n~ GitHub link: github.com/shashankkp247\n~ Function of the Code: To print the reversed version of the 3 digit number prompted from the user\n')

#asking for 3 digit integer input which will be considered as string
num = input("Enter a 3 digit number from 001 to 999 \n(else the output result will be undesired) : ")

#to check if the number is between 001 & 999 we will convert the given input as an int only for checking purposes
#but if we would have taken the input itself as int the 0's coming before a 1 or 2 digit number will truncated or cut off.
n = int(num)

if int(n) <= 0 or int(n) >= 999:
    print('usage:"Enter number between 100 to 999"')
    exit(1)

#making a dummy variable that will help in our reversing process
str = ""

# a for to reverse the order of the number
for i in num:
    str = i + str

#printing the results
print(f'The reversed 3 digit number is "{str}"')
