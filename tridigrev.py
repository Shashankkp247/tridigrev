#intro
print('\n***PROJECT DETAILS***\n\n***Function of the Code: To print the reversed version of the 3 digit number prompted from the user***\n')
#here the \n just means go to next which means that the letters after will be printed in the next line
#I am using it to just clean up the codes intro part
print('~ Project name: 3_digit_number_reverser\n~ Creator name: Shashank.k.puttappanavar')
print('~ GitHub ID: Shashankkp247\n~ GitHub link: github.com/shashankkp247\n')
print("~ GitHub source-code link: https://github.com/Shashankkp247/tridigrev/blob/main/tridigrev.py \n")

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

#printing the results with a smile
print(f'\n:) The reversed number is "{str}"\n')
