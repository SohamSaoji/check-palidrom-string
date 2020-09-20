# function which return reverse of a string
 
def checkPalindrome(i):
    return i == i[::-1]
 
i = "racecar"
check = checkPalindrome(i)
 
if check:
    print("Yes")
else:
    print("No")