import math

def find_prime(position):
    """
    Finds the n-th prime number
        position - int - the position of the prime number to be found
    Returns - int - the prime number at position
    """
    primes = [2,3,5,7,11,13]

    if position <= len(primes):
        return primes[position-1]

    cur_pos = len(primes)-1
    check = 15

    primes = primes[1:] # remove the 2 because no even numbers will be checked

    while cur_pos < position:
        check_prime = True
        check_sqrt = int(math.sqrt(check))
        for prime in primes:
            #if the current prime is greater than the square root it cannot be
            #a factor, and no primes past it can be either
            if prime > check_sqrt:
                break
            #The number is not prime
            if check % prime == 0:
                check_prime = False
                break
        #If the number is prime add it to the prime list
        if check_prime:
            primes += [check]
            cur_pos += 1
        check += 2
    return(primes[position-2]) # -1 to convert to index, -1 because 2 is gone

def main():
    print(str(find_prime(10001)))

if __name__ == "__main__":
    main()
