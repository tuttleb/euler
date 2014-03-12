def is_palindrome(value):
    """
    Determines if the input is a palindrome
        value - The number or string to check
    Returns - True if value is a palindrome, False otherwise
    """
    if value is None:
        return False
        
    value = str(value)

    if value == "":
        return True

    first = 0
    last = len(value)-1
    while last >= first:
        if value[first] != value[last]:
            return False
        first += 1
        last -= 1
    return True

def main():
    biggest = 0
    #iterate over all multiplication combinations
    for num_a in range(999, 99, -1):
        for num_b in range(num_a, 99, -1):
            result = num_a * num_b
            if is_palindrome(result) and result > biggest:
                biggest = result
    print(biggest)

if __name__ == "__main__":
    main()
