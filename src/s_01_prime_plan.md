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
    - Divide by all other prime numbers? - if it's divisible, it's NOT prime
        - ↑ How do we know all other prime numbers?
    - Divide by all other numbers from 2 to the given
        - laborious, but it'll work for sure


# Write a program to print all the prime numbers up to a number given on the command line.

## Understand

- How will user input number?
    - Command line input
- Numbers only?
    - One number only. TypeError exception handling
- What will the output be?
    - Array of all numbers that are prime