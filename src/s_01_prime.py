import time
import math

def is_prime(num):
    prime = True
    # Trial division: Loop through all numbers until the given
    # If none are divisible without a remainder, the number is prime
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    return prime

def all_prime_until(max):
    all_nums = [True for i in range(max+1)]
    # Our max pointer is the sqrt of our max number. Round up to an int
    max_pointer = math.ceil(math.sqrt(max))
    for p in range(2, max_pointer):
        if all_nums[p] == True:
            not_prime = p**p
            while not_prime < len(all_nums):
                all_nums[not_prime] = False
                not_prime += p
    prime_nums = [i for i,val in enumerate(all_nums) if val == True]
    return prime_nums[2:]

def print_and_wait(message="Please try again.", interval=0.5):
    print(message)
    time.sleep(interval)

def main():
    
    """
    We will always loop until loop == False
    The display determines which specific loop we're inside of:
        0 -> Main section
        1 -> is_prime section
        2 -> all_primes_until section
    """
    display = 0
    loop = True
    while loop:

        # Main section
        while(display == 0):
            print(          "\n\nWelcome to the Prime Program!")
            print(          "Select which Program you would like to use:")
            user_in = input("[1] Is this number prime?\n[2] All prime numbers up to this number\n[9] Exit\n")
            # Try to parse to an int, if no success try again
            try:
                decision = int(user_in)
                if decision == 9:
                    loop = False
                    break;
                elif decision == 1 or decision == 2:
                    # If a valid decision, change the display and break
                    display = decision
                    break;
                else: print_and_wait("Please enter a valid number.")
            except:
                print_and_wait("Please enter a valid number.")

        # is_prime section
        while(display == 1):
            print("\n\nFind out if a number(no decimals, please!) is prime.")
            print("To go back to the menu, type \"back\".")
            user_in = input("Please enter a number:")

            if user_in == "back": 
                display = 0
                break;

            try:
                # Valid number? run the function, and then return to the main menu
                num = int(user_in)
                print_and_wait(str(is_prime(num)), 1.5)
                display = 0
                break;
            except:
                print_and_wait("That's not a valid input!\nRemember, only numbers without decimals, please!")

        # all_prime_until section
        while(display == 2):

            print("\n\nFind all of the prime numbers up to a given max.")
            print("To go back to the menu, type \"back\".")
            user_in = input("Please enter a number:")

            if user_in == "back": 
                display = 0
                break;

            try:
                # Valid number? run the function, and then return to the main menu
                num = int(user_in)
                print_and_wait(str(all_prime_until(num)), 3.5)
                display = 0
                break;
            except:
                print_and_wait("That's not a valid input!\nRemember, only numbers without decimals, please!")




if __name__ == "__main__":
    main()