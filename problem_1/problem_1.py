def main():
    """
    adds every multiple of 3 up to 1000, then adds every multiple of 5 up to 
    1000 that is not also a multiple of 3
    """

    total = 0
    for multiple in range(3,1000,3):
        total += multiple

    for multiple in range(5,1000,5):
        if multiple % 3 is not 0:
            total += multiple

    print("The solution is: " + str(total))

if __name__ == "__main__":
    main()
