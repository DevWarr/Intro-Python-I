import time
# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    return num % 2 == 0

# Read a number from the keyboard
loop = True
while(loop):
    num = input("Enter a number: ")
    try:
        num = int(num)
        loop = False;
    except:
        print("this is not a number!")
        time.sleep(0.5)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if is_even(num): print("Even!")
else: print("Odd!")