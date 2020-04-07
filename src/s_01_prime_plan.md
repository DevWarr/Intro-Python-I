# Write a program to determine if a number, given on the command line, is prime.

1. How can you optimize this program?
2. Implement [The Sieve of Erathosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes),
   one of the oldest algorithms known (ca. 200 BC).

## Understand

- How will user input number?
    - Command line input
- Numbers only?
    - One number only. TypeError exception handling
- What will the output be?
    - Boolean (True/False)

## Plan

- Trial division
    [ ] Divide by all other prime numbers? - if it's divisible, it's NOT prime
        - ↑ How do we know all other prime numbers?
    [x] Divide by all other numbers from 2 to the given
        - laborious, but it'll work for sure


# Write a program to print all the prime numbers up to a number given on the command line.

## Understand

- How will user input number?
    - Command line input
- Numbers only?
    - One number only. TypeError exception handling
- What will the output be?
    - List of all numbers that are prime

## Plan

- Sieve of Eratosthenes
    1. Create an list 
        - all values True
        - length of our given number plus one (so our index actually goes up to our maximum number)
    2. Create a pointer that starts at 2
    3. Loop from the pointer to the sqrt(given number) (or the next integer up)
    4. iterate through the list
        - start at the pointer's index         ( Example, starting at p = 5       )
        - increment by the pointer's value     ( go to 10, then 15, then 20, etc  )
        - Change each value in the list to False, if it isn't already
    5. Move the pointer to the next True value in the list, and repeat step 4.
    6. Once the loop is complete, return a new list
        - New list's values should be the indices of all True values in the old list
        - Exclude 0 and 1 from the New list
