def divisible_under_limit(limit, num):
    """
    Determines if a number is divisible by all values up to a given limit
        limit - int - The maximum number to check inclusive
        num - int - The number that is being dividedd
    """ 
    for i in range(2, limit+1):
        if num % i != 0:
            return False
    return True

def main():
    current = 20
    while not divisible_under_limit(20, current):
        current += 20
    print(current) 

if __name__ == "__main__":
    main()
