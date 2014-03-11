import math

def is_prime(num):
    """
    Determines if a number is prime
        num int - the number to check
    returns bool - True if num is prime, False otherwise
    """
    #pre-eliminate even numbers and numbers less than two
    if num < 2 or num % 2 == 0:
        return False
    
    #treats 2 as a special case to allow for incrementing by two later on
    if num == 2: 
        return True
    
    for i in range(3,int(math.sqrt(num)),2):
        if num % i == 0:
            return False
    return True

def main():
    potential_primes = []
    for i in range(3, int(math.sqrt(600851475143)), 2):
        if 600851475143 % i == 0:
            potential_primes = [i] + potential_primes

    print("Determining Result")
    for value in potential_primes:
        if is_prime(value):
            print(value)
            break
if __name__ == "__main__":
    main()
