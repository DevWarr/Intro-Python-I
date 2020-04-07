import time

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
    return

def main():
    num = 0
    loop = True
    while loop:
        print("Find out if a number(no decimals, please!) is prime.")
        user_in = input("Please enter a number:")
        try:
            num = int(user_in)
            loop = False
        except TypeError:
            print("That's not a valid number!")
            print("Remember, only numbers without decimals, please!\n")
            time.sleep(0.5)
    print(is_prime(num))




if __name__ == "__main__":
    main()