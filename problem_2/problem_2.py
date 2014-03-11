def main():
    #the sum to return
    total = 2

    #the last two fibonaccia numbers
    fib_1 = 1
    fib_2 = 2
    #the next fibonacci number
    next_fib = fib_1+fib_2
    
    while next_fib < 4000000:
       if next_fib % 2 == 0: total += next_fib
       
       fib_1 = fib_2
       fib_2 = next_fib 
       next_fib = fib_1 + fib_2

    print("The solution is: " + str(total))

if __name__ == "__main__":
    main()
